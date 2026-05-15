from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
import os
import sys


# Use a variable so we can validate cloud usage easily
MODEL = os.getenv("OLLAMA_MODEL", "granite4.1:3b")

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

@tool
def addition(a: float, b: float) -> float:
    """Additionne deux nombres et retourne le résultat."""
    return a + b

tools = [addition]
tools_by_name = {tool.name: tool for tool in tools}

# ChatOllama avec outils LangChain
model_ollama = ChatOllama(model=MODEL, temperature=0)
model_with_tools = model_ollama.bind_tools(tools)

messages = [
    SystemMessage(content="Tu es un assistant utile. Pour les additions, utilise l'outil addition."),
    HumanMessage(content="Combien font 123.5 + 456.7 ?")
]

# 1. Le modèle décide s'il doit appeler un outil.
ai_message = model_with_tools.invoke(messages)
messages.append(ai_message)

print("=== Appels d'outils demandés par le modèle ===")
print(ai_message.tool_calls)
print()

if not ai_message.tool_calls:
    print("Le modèle n'a pas demandé d'appel d'outil.")
    print("Réponse directe du modèle :")
    print(ai_message.content)
    sys.exit(0)

# 2. Python exécute les outils demandés, puis ajoute les résultats à la conversation.
for tool_call in ai_message.tool_calls:
    selected_tool = tools_by_name[tool_call["name"]]
    tool_result = selected_tool.invoke(tool_call["args"])
    messages.append(
        ToolMessage(
            content=str(tool_result),
            tool_call_id=tool_call["id"],
        )
    )

# 3. Le modèle reçoit le résultat de l'outil et répond à l'utilisateur.
final_response = model_with_tools.invoke(messages)

print("=== Réponse finale ===")
print(final_response.content)
