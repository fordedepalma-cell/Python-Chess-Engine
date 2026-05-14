# This script is intended for testing AI-related functionality of the chess engine.

from openai import OpenAI
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY
)
model = "gpt-5.2"
messages = []

def add_user_message(text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

params = {
    "model": model,
    "messages": messages
}

chat_completion = client.chat.completions.create(**params)

print(chat_completion.choices[0].message.content)

# Commented out code
"""
# Math tutor
messages = [
    {
        "role": "system",
        "content": "You are a patient math tutor. Do not directly answer a student's questions. Guide them to a solution step by step. Make the teaching process as interactive as possible for the student."
    }
]

# client = Groq(api_key=GROQ_API_KEY)
# model = "<any model here>"
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY
)
model = "gpt-5.2"

def add_user_message(text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

session_running = True

def chat():
    global session_running

    print("-----------------------------")
    print(f"Using the {model} model")
    prompt = input("Ask me anything: \n")

    if prompt == "/quit":
        session_running = False
        return None

    add_user_message(prompt)

    params = {
        "model": model,
        "messages": messages
    }

    chat_completion = client.chat.completions.create(**params)

    return chat_completion.choices[0].message.content

while session_running:
    response = chat()
    if response is None:
        break
    add_assistant_message(response)
    print(response)

print("Your session is now expired")
"""
