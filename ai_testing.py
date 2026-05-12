# This script is intended for testing AI-related functionality of the chess engine.

from openrouter import OpenRouter
import requests
import json
from python_dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

with OpenRouter(api_key=OPENROUTER_API_KEY) as client:
    response = client.chat.send(
        model="openai/gpt-5.2",
        messages=[
            {"role": "user", "content": "Hello there!"}
        ],
    )
    print(response.choices[0].message.content)

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    },
    data=json.dumps({
        "model": "openai/gpt-5.2",
        "messages": [
            {
                "role": "user",
                "content": "Hello there!"
            }
        ]
    })
)

print(response.json())
