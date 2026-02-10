from google import genai
import os
from dotenv import load_dotenv
import asyncio
load_dotenv(override=True)

try:

    KEY=os.getenv("GEMINI_API_KEY")
    

    print("KEY LOADED SUCCESSFULLY",f"{KEY}")
    #client=genai.Client(api_key=f"{KEY}") Method:I
    client=genai.Client(api_key=KEY) # Method:II
    #Both Method Works provided .env is of type GEMINI_API_KEY="afkcamk"
    
    print("AI Response: ")

    #Chapter I: Streamming the responses(Syncronous)
    # for chunk in client.models.generate_content_stream(model='gemini-2.5-flash', contents='write story in 130 words'):
        
    #     print(chunk.text, end='')


    #Chapter II:Not stream response(Syncronous)

    # response=client.models.generate_content(model='gemini-2.5-flash',contents="who are you?")
    # print(response.text)


    #Chapter III:Streamming(Asyncronous)
    #see chapter3.py
  
        
    
except Exception as e:
    print("Exeption--->",e)







