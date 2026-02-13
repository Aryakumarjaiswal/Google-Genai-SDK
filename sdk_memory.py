from google import genai
import os
from dotenv import load_dotenv
import asyncio

import time
load_dotenv(override=True)

try:
    s=time.time()
    KEY=os.getenv("GEMINI_API_KEY")
    

    print("KEY LOADED SUCCESSFULLY",f"{KEY}")
    # client=genai.Client(api_key=f"{KEY}") Method:I
    client=genai.Client(api_key=KEY) # Method:II
    #Both Method Works provided .env is of type GEMINI_API_KEY="afkcamk"
    
    print("AI Response: ")
    #Gemini provided inbuild chat module for memory.The SDK manages the history list for you.YEH NAHI CALEGA-> response=client.models.generate_content(model="gemini-2.0-flash",contents="Hi,I'm Aryakumar")
    chat=client.chats.create(model="gemini-2.0-flash")
    response=chat.send_message("Hi I'm Arya!!")
    print(response.text)

        
    
except Exception as e:
    print("Exeption--->",e)







