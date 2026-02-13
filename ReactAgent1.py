from google import genai
from google.genai import types

from dotenv import load_dotenv
import os

load_dotenv(override=True)
KEY=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=KEY)
# --- Tools ---
def get_stock_price(symbol: str) -> float:
    """Retrieves the current stock price for a given symbol."""
    print(f"\n[Tool Activity] Checking stock price for {symbol}...")
    mock_stocks = {"GOOG": 175.50, "MSFT": 420.00, "AAPL": 180.00}
    return mock_stocks.get(symbol.upper(), 0.0)

def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    print(f"\n[Tool Activity] Multiplying {a} * {b}...")
    return a * b

# --- The ReAct Agent ---
def run_react_agent():
    
    # 1. The System Prompt (Crucial for ReAct)
    # We tell the model to explicitly "Think" before acting.
    system_instruction = """
    You are a helpful AI assistant called 'ReActBot'.
    
    CRITICAL INSTRUCTION:
    Before using any tool, you must explicitly state your Thought process.
    Format your response as:
    Thought: [Your reasoning here]
    """

    # 2. Configure the Client
    chat = client.chats.create(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            tools=[get_stock_price, multiply],
            temperature=0.0, # Keep it factual
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=False,
                maximum_remote_calls=5 # Prevent infinite loops
            )
        )
    )

    # 3. The User Query
    query = "If I buy 10 shares of Google and 5 shares of Microsoft, how much total money do I need?"
    print(f"User: {query}")

    # 4. Execution
    response = chat.send_message(query)
    
    print("\n--- Final Agent Response ---")
    print(response.text)

run_react_agent()
########################### output
# Breakdown of the ReAct Output:
# When you run this, you will see something very interesting happen in the console (due to the print statements in the tools):
# Thought: The model thinks: "I need to find the price of GOOG and MSFT, then multiply the quantities, then add them up."
# Action 1: Calls get_stock_price("GOOG").
# Action 2: Calls get_stock_price("MSFT").
# Action 3: Calls multiply(175.50, 10).
# Action 4: Calls multiply(420.00, 5).
# Final Answer: "You need $3,855.00."
# Summary
# Memory: Use client.chats.create() and chat.send_message(). The object stays alive and keeps track of the conversation.
# Function Calling: Define standard Python functions and pass them in the tools list. Set automatic_function_calling to true for the easiest experience.
# ReAct Agent: Combine Tools with a System Instruction that forces the model to explain its reasoning ("Thought:") before it calls the functions.
