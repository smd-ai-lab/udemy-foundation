from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_ollama import ChatOllama


# Ollama
model_ollama = ChatOllama(model="granite4.1:30b", temperature=0.2)

# Messages textuels
system_msg = SystemMessage(content="Vous êtes un expert en programmation Python.")
human_msg = HumanMessage(content="Comment utiliser les décorateurs ?")
ai_msg = AIMessage(content="Les décorateurs sont des fonctions qui modifient...")

# Envoi d'une conversation complète
conversation = [system_msg, human_msg]
reponse = model_ollama.invoke(conversation)

print("=============================== Réponse du modèle ===")
print(reponse.content)
print()

# Conversation avec historique (messages précédents + nouvelle question)
conversation_with_history = [system_msg, human_msg, ai_msg, HumanMessage(content="Donne-moi un exemple concret.")]
reponse = model_ollama.invoke(conversation_with_history)

print("================================== Réponse avec historique ===")
print(reponse.content)