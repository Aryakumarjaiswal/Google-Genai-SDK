from google import genai 
from google.genai import types
from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]


load_dotenv(override=True)
KEY=os.getenv("GEMINI_API_KEY")


client=genai.Client(api_key=KEY)

response=client.models.generate_content(model="gemini-3-flash-preview",
                                        contents="Who is tony stark?",
                                        config=types.GenerateContentConfig( #Defines thinking capibility
        thinking_config=types.ThinkingConfig(thinking_level="low"),
        temperature=0.1,#controls randomness
        system_instruction="You're world's best roaster.On recieving question just brutally roast user."
    ),)
print(response.text)
