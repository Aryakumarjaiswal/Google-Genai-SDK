#######3 Asyncronous streamming
import asyncio
from google import genai
import os
from dotenv import load_dotenv
load_dotenv(override=True)

KEY=os.getenv("GEMINI_API_KEY")


# 1. Function ko 'async' banao

async def stream_story():
    client = genai.Client(api_key=KEY) 
    
    print("AI is thinking...\n")

    # 2. 'await' lagao stream start karne ke liye
    # client.aio use karna zaroori hai (aio = Asynchronous IO)
    response_stream = await client.aio.models.generate_content_stream(
        model='gemini-2.5-flash', 
        contents='Tell me a story in 80 words.'
    )

    # 3. 'async for' se har ek tukde (chunk) ko pakdo
    async for chunk in response_stream:
        # chunk.text mein actual words hote hain
        if chunk.text:
            print(chunk.text, end="", flush=True) 

# 4. Script ko run karne ka tarika
if __name__ == "__main__":
    asyncio.run(stream_story())
