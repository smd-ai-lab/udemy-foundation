import os
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field


# Use a variable so we can validate cloud usage easily
MODEL = os.getenv("OLLAMA_MODEL", "ollama:granite4.1:3b")

# Quick environment validation when using a cloud model
if ":cloud" in MODEL:
    api_key = os.getenv("OLLAMA_API_KEY")
    host = os.getenv("OLLAMA_HOST")
    if not api_key:
        print("ERROR: Using a cloud Ollama model requires OLLAMA_API_KEY to be set.")
        print("Set it with: export OLLAMA_API_KEY=\"your_key\"")
        sys.exit(1)
    if not host:
        print("NOTE: OLLAMA_HOST not set; defaulting to https://api.ollama.com")
        os.environ["OLLAMA_HOST"] = "https://api.ollama.com"

# Ollama
model_ollama = ChatOllama(model=MODEL, temperature=0.2)

class ContactInfo(BaseModel):
    """Contact information for a person."""
    name: str = Field(description="The name of the person")
    email: str = Field(description="The email address of the person")
    phone: str = Field(description="The phone number of the person")

agent = create_agent(
    model=model_ollama,
    response_format=ContactInfo  # Auto-selects ProviderStrategy
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, (555) 123-4567"}]
})

print(result["structured_response"])