import os
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.agents.middleware import PIIMiddleware
from langchain.tools import tool

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

@tool
def email_tool(a: float, b: float) -> float:
    """retourne un email d'entreprise"""
    return "team123@theworldcompany.org"

agent = create_agent(
    model=model_ollama,
    tools=[email_tool],
    middleware=[
        # Redact emails in user input before sending to model
        PIIMiddleware(
            "email",
            strategy="redact",
            apply_to_input=True,
        ),
        # Mask credit cards in user input
        PIIMiddleware(
            "credit_card",
            strategy="mask",
            apply_to_input=True,
        ),
        # Block API keys - raise error if detected
        PIIMiddleware(
            "api_key",
            detector=r"sk-[a-zA-Z0-9]{32}",
            strategy="block",
            apply_to_input=True,
        ),
    ],
)

# When user provides PII, it will be handled according to the strategy
response = agent.invoke({
    "messages": [{"role": "user", "content": "Reply with the email of my team , or stephane.metairie@myworldcompany.org , note than my card is 5105-1051-0510-5100"}]
})

# Print the whole conversation
for msg in response["messages"]:
    role = msg.type if hasattr(msg, "type") else msg.get("role", "unknown")
    content = msg.content if hasattr(msg, "content") else msg.get("content", "")
    print(f"[{role}]: {content}")
    print("---")