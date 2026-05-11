# ollama

Micromamba doit etre installé.


```bash
micromamba activate
micromamba shell init
micromamba create -n ollama-test python=3.13
micromamba activate ollama-test
pip install -r requirements.txt
# modeles utilisés
ollama pull gemma3:27b-cloud
ollama pull nomic-embed-text
ollama pull deepseek-r1:1.5b
ollama pull granite4.1:3b
OLLAMA_HOST=http://localhost:11434/ SSL_CERT_FILE= python ollama-test.py 
OLLAMA_HOST=http://localhost:11434/ SSL_CERT_FILE= python ollama-vision.py 
OLLAMA_HOST=http://localhost:11434/ SSL_CERT_FILE= python ollama-embeddings.py 
```

