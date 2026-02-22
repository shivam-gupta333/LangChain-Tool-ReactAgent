from langchain_core.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import requests
from langchain.agents import create_agent

load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-120b")

@tool
def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    """Get the exchange rate between two currencies."""
    # Correct URL for pair conversion
    url = f"https://v6.exchangerate-api.com/v6/af41fc3a32e9338be04c6827/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    
    # Error handling for non-200 responses
    if response.status_code != 200:
        raise ValueError(f"HTTP Error: {response.status_code}")
        
    data = response.json()
    if data.get("result") == "success":
        return data.get("conversion_rate")
    else:
        error_msg = data.get("error-type", "Unknown error")
        raise ValueError(f"API Error: {error_msg}")

@tool
def convert_currency(amount: float, rate: float) -> float:
    """Convert an amount from one currency to another."""
    return round(amount * rate, 2)


agent = create_agent(
    model=llm,
    tools=[get_exchange_rate, convert_currency],
    system_prompt="You are a helpful assistant.",
)

response = agent.invoke({"messages":[{"role":"user","content": "What is the exchange rate between USD and INR? Convert 100 USD to INR"}]})
print(response["messages"][-1].content)