# GPT-2 for Story Generation

## Intro
GPT-2 is a language model that predicts the next word in a sentence using the information from previous words. GPT-2 is created by OpenAI in February 2019 and is able to perform a wide variety of NLP tasks such as question answering, text generation and language translation.

## Limitation of previous NLP models
Previous NLP models such as RNN or GRU are trained in a supervised manner to perform only one task with datasets which belong to the same domain. However, the performance of these kind of model decreases when there is a slight change in the distribution of test data compared to data the model is trained on. 

This is significant to models deployed in a real environment setting:
1. Inputs to the model comes in different forms.  
2. The performance of the model decreases when it is asked to perform a task that it is not trained to do. 
3. Researchers need to go through the laborious task of labelling the dataset to train the model to perform a different task.

## Contributions of GPT-2
GPT-2 is a general purpose learner which can perform many down-stream tasks without any modifications in the model's architecture and parameters. When a large language model like GPT-2 is trained on a large and diverse dataset it is able to perform well across many domains and tasks. GPT-2 has achieved state of the art performance on 7 out of 8 benchmark language modeling datasets.

-------------------------------------------------------

## Story Generation

**Run locally**

**STEP 1 - Download GPT-2**
```
pip install -r requirements.txt
python download_model.py
```

**STEP 2 - Run flask API**
```
flask run
```

OR

**Run in docker container**

**STEP 1 - docker build**
```
docker build -t gpt
```

**STEP 2 - docker run**
```
docker run -p 5000:5000 -t gpt
```

**STEP 3 - Send a POST request with a JSON that contains the input text**

The JSON should have the following structure:

```
{
    "input": "<ENTER INPUT TEXT>"
}
```

Send POST request to: (using Postman or Insomnia)
```
http://0.0.0.0:5000/
```
TAKE NOTE: The model might take 1 minute to send the result back

--------------------------------------------------------

## Result

GPT-2 is used to generate story snippets for 3 different genres - Romance, Crime and Politics. 

### Genre: Romance

**Input:** 

I have a crush on this girl, her name is Anne. She has watery big eyes and rosy cheeks. On Valentines day, I decide to ask her out.

**Output:** 

I have a crush on this girl, her name is Anne. She has watery big eyes and rosy cheeks. On Valentines day, I decide to ask her out.

"I love you, Anne," I say. "I'm so glad you're here."

She smiles. "Thank you," she says. "It's been so long since I've seen you. I'm so happy to see you again."


### Genre: Crime

**Input:** 

The detective reach the crime scene

**Output:** 

The detective reach the crime scene and find the body of a man who had been shot in the head.

The suspect is described as a black man in his 20s. He was last seen wearing a black hooded sweatshirt, black pants, and black shoes. He is believed to be in his late 20s or early 30s with a dark complexion. He has dark hair, brown eyes, and blue eyes. He may have a tattoo on his right arm.


### Genre: Politics

**Input:** 

Drugs should not be legalized

**Output:** 

Drugs should not be legalized in the United States."

The bill, which passed the House of Representatives last week, was introduced by Rep. Steve King (R-Iowa), a member of the House Judiciary Committee.

"We need to make sure that we don't legalize marijuana for recreational use," King said in a statement. "This bill is a step in the right direction, but it's not the end of the road."

-----------------------------------------------------------------------------

## Further Improvements
1. Improve the inference speed of the model (currently takes around 1 minute)
2. Train the GPT-2 model on doamin-specific texts (e.g: train model on multiple resumes to create resume generator)



