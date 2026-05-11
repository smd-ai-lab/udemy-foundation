import ollama
import base64
from PIL import Image

# Charger et encoder une image
image_path = 'photo.jpg'
with open(image_path, 'rb') as img_file:
    image_base64 = base64.b64encode(img_file.read()).decode('utf-8')

# Analyser l'image
response = ollama.chat(
    model='gemma3:27b-cloud',
    messages=[{
        'role': 'user',
        'content': 'Décris ce que tu vois sur cette image.',
        'images': [image_base64]
    }]
)

print(response['message']['content'])