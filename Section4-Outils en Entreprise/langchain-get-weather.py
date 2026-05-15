import os
import sys
from langchain.agents import create_agent
from langchain_ollama import ChatOllama


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model=ChatOllama(model="granite4.1:3b", temperature=0),
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)

print(result)
