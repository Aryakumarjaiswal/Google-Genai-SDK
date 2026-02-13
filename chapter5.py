from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv(override=True)
KEY=os.getenv("GEMINI_API_KEY")

client = genai.Client()
chat = client.chats.create(model="gemini-3-flash-preview")

response = chat.send_message_stream("I have 2 dogs in my house.")
for chunk in response:
    print(chunk.text, end="")

response = chat.send_message_stream("How many paws are in my house?")
for chunk in response:
    print(chunk.text, end="")

for message in chat.get_history():
    print(f'role - {message.role}', end=": ")
    print(message.parts[0].text)
