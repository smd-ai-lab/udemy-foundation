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

reponse = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)

# Print the whole conversation
for msg in reponse["messages"]:
    role = msg.type if hasattr(msg, "type") else msg.get("role", "unknown")
    content = msg.content if hasattr(msg, "content") else msg.get("content", "")
    print(f"[{role}]: {content}")
    print("---")