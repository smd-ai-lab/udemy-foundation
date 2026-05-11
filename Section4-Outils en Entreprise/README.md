# ollama

Micromamba doit etre installé.


```bash
micromamba activate
micromamba shell init
micromamba create -n ollama-chat python=3.13
micromamba activate ollama-chat
pip install -r requirements.txt
OLLAMA_HOST=http://localhost:11434/ SSL_CERT_FILE= python ollama-chat.py 
```
