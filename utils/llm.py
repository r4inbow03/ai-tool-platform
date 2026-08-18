import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_client():
    return OpenAI(
        api_key = os.getenv("OPENROUTER_API_KEY"),
        base_url = "https://openrouter.ai/api/v1"
    )

def call_llm(prompt: str, model: str):
    client = get_client()

    response = client.chat.completions.create(
        model = model,
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content