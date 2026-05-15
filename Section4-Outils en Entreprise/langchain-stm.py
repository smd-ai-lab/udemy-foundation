import os
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver  


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

# Création du sauvegarde mémoire
checkpointer = InMemorySaver()

agent = create_agent(
  model=model_ollama,
  checkpointer=checkpointer # Active la persistance
)

# Session 1 - L'agent "se souvient"
config = {"configurable": {"thread_id": "utilisateur-123"}}

reponse = agent.invoke(
  {"messages": [{"role": "user", "content": "Je m'appelle utilisateur-123"}]},
  config=config
)

# Session 2 - L'agent a gardé le contexte
reponse = agent.invoke(
  {"messages": [{"role": "user", "content": "Quel est mon nom ?"}]},
  config=config
)

# Print the whole conversation
for msg in reponse["messages"]:
    role = msg.type if hasattr(msg, "type") else msg.get("role", "unknown")
    content = msg.content if hasattr(msg, "content") else msg.get("content", "")
    print(f"[{role}]: {content}")
    print("---")