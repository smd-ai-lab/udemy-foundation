import ollama
import json

# Définir une fonction météo (simulation)
def get_temperature(city: str) -> str:
    """Retourne la température pour une ville donnée"""
    temperatures = {
        'Paris': '22°C',
        'Lyon': '19°C',
        'Marseille': '25°C',
        'New York': '18°C',
        'London': '15°C'
    }
    return temperatures.get(city, 'Inconnue')

# Définir la spécification de l'outil pour Ollama
tools = [{
    'type': 'function',
    'function': {
        'name': 'get_temperature',
        'description': 'Obtenir la température actuelle dans une ville',
        'parameters': {
            'type': 'object',
            'properties': {
                'city': {
                    'type': 'string',
                    'description': 'Nom de la ville',
                }
            },
            'required': ['city'],
        },
    },
}]

# Le modèle va décider d'appeler ou non l'outil
response = ollama.chat(
    model='granite4.1:3b',
    messages=[{'role': 'user', 'content': "Quel temps fait-il à Paris ?"}],
    tools=tools,
)

# Vérifier si le modèle veut appeler un outil
if response['message'].get('tool_calls'):
    for tool_call in response['message']['tool_calls']:
        if tool_call['function']['name'] == 'get_temperature':
            # Extraire les arguments (déjà un dict, pas une string JSON)
            args = tool_call['function']['arguments']
            if isinstance(args, str):
                args = json.loads(args)
            city = args['city']
            
            # Exécuter la fonction
            result = get_temperature(city)
            print(f"Température à {city}: {result}")