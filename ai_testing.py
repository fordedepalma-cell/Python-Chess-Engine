# This script is intended for testing AI-related functionality of the chess engine.

from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(
    api_key=API_KEY
)
model = "groq/compound"

class ValidationStatus(BaseModel):
    is_valid: bool
    syntax_errors: list[str]

class SQLQueryGeneration(BaseModel):
    query: str
    query_type: str
    tables_used: list[str]
    estimated_complexity: str
    execution_notes: list[str]
    validation_status: ValidationStatus

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": "You are a SQL expert. Generate structured SQL queries from natural language descriptions with proper syntax validation and metadata.",
        },
        {"role": "user", "content": "Find all customers who made orders over $500 in the last 30 days, show their name, email, and total order amount"},
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "sql_query_generation",
            "schema": SQLQueryGeneration.model_json_schema()
        }
    }
)

sql_query_generation = SQLQueryGeneration.model_validate(json.loads(response.choices[0].message.content))
print(json.dumps(sql_query_generation.model_dump(), indent=2))

# messages = []
#
# def add_user_message(text):
#     user_message = {"role": "user", "content": text}
#     messages.append(user_message)
#
# def add_assistant_message(text):
#     assistant_message = {"role": "assistant", "content": text}
#     messages.append(assistant_message)
#
# params = {
#     "model": model,
#     "messages": messages,
#     "temperature": 0.5,
#     "max_completion_tokens": 1024,
#     "top_p": 1,
# }

# add_user_message("Let me know what you want me to generate, and I'll generate just the actual, raw data for you.")
# add_user_message("Generate three different sample AWS CLI commands that are very short.")
# chat_completion = client.chat.completions.create(**params)
# print(chat_completion.choices[0].message.content)

"""
stream = client.chat.completions.create(**params)

# Print the incremental deltas returned by the LLM.
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content is not "*" or content is not None:
        print(content, end="")


# Commented out code
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
