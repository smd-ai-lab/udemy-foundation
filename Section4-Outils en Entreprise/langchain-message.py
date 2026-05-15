from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_ollama import ChatOllama
import os

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

# Messages textuels
system_msg = SystemMessage(content="Vous êtes un expert en programmation Python.")
human_msg = HumanMessage(content="Comment utiliser les décorateurs ?")
ai_msg = AIMessage(content="Les décorateurs sont des fonctions qui modifient...")

# Envoi d'une conversation complète
conversation = [system_msg, human_msg]
reponse = model_ollama.invoke(conversation)

print("=== Réponse du modèle ===")
print(reponse.content)
print()

# Conversation avec historique (messages précédents + nouvelle question)
conversation_with_history = [system_msg, human_msg, ai_msg, HumanMessage(content="Donne-moi un exemple concret.")]
reponse = model_ollama.invoke(conversation_with_history)

print("=== Réponse avec historique ===")
print(reponse.content)