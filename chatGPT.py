import openai
import os

async def chatGPT(question):
    openai_token = os.getenv('OPENAITOKEN')
    openai.api_key = openai_token
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    
    return completion.choices[0].text

