import os
from ollama import Client, ChatResponse

# Create client with SSL verification disabled for local development
client = Client(host=os.getenv('OLLAMA_HOST', 'http://localhost:11434'), verify=False)

response: ChatResponse = client.chat(model='granite4.1:3b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)