from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import os


file_dir_path = os.path.dirname(os.path.realpath(__file__))
saved_model_path = os.path.join(file_dir_path, "gpt2_model")

# Load pre-rained tokenizer
gpt2tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Load pre-trained GPT-2 model
gpt2 = TFGPT2LMHeadModel.from_pretrained(
    "gpt2", pad_token_id=gpt2tokenizer.eos_token_id
)

gpt2.save_pretrained(saved_model_path)
