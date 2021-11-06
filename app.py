from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import tensorflow as tf
import json
from flask import Flask, request,jsonify
import os


file_dir_path = os.path.dirname(os.path.realpath(__file__))
saved_model_path = os.path.join(file_dir_path, 'gpt2_model')
tokenizer_path = os.path.join(file_dir_path, 'tokenizer')

app = Flask(__name__)


def generate_texts(input_string):
    # load tokenizer
    gpt2tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    # load trained model
    gpt2 = TFGPT2LMHeadModel.from_pretrained(saved_model_path, pad_token_id=gpt2tokenizer.eos_token_id)

    input_ids = gpt2tokenizer.encode(input_string, return_tensors='tf')

    beam_output = gpt2.generate(
        input_ids,
        max_length=250,
        num_beams=5,
        no_repeat_ngram_size=3,
        early_stopping=True
    )
    return gpt2tokenizer.decode(beam_output[0], skip_special_tokens=True)


@app.route('/', methods=['POST'])
def predict():
    data = request.get_json()
    input_string = data['input']
    result = generate_texts(input_string)
    return jsonify({'result': json.dumps(result)})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


    
    