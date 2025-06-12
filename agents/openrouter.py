import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def call_openrouter(user_prompt, system_prompt="You are a helpful assistant.", model="openai/gpt-4o", temperature=0.4):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature
    )
    
    return response.choices[0].message.content
