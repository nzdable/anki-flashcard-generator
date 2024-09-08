import os
import openai
import clipboard
import json

# Setting OpenAI API key
openai.api_key = os.environ[""]

# Getting content from clipboard
clipboard_content = clipboard.paste()

# Creating conversation with ChatGPT
messages = [
    {"role": "system", "content":  "Hello"},
    {"role": "system", "content":  "Create Anki flashcards with the following format: wh-questions;answer next line wh-questions;answer etc...{clipboard_content}."},
]

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    temperature=0.7,
    max_tokens=2000
)

generated_flashcards = response["choices"][0]["message"]["content"]

# Save flashcards to a file
with open("flashcards.txt", "w") as f:
    f.write(generated_flashcards)

print("Flashcards saved to 'flashcards.txt'")