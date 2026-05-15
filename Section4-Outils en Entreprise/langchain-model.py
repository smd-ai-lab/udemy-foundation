from langchain_ollama import ChatOllama


# Ollama
model_ollama = ChatOllama(model="granite4.1:3b", temperature=0.7)
reponse = model_ollama.invoke("Bonjour le monde !")

print(reponse.content)