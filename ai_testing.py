# This script is intended for testing AI-related functionality of the chess engine.

from openrouter import OpenRouter
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print(OPENROUTER_API_KEY, GROQ_API_KEY)

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)

# response = requests.post(
#     url="https://openrouter.ai/api/v1/chat/completions",
#     headers={
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#     },
#     data=json.dumps({
#         "model": "openai/gpt-5.2",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "Hello there!"
#             }
#         ]
#     })
# )
#
# print(response.json())
