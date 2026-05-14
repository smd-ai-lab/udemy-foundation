# Udemy

 
## configuration locale

### Git

```bash
# windows
git config --global core.sshCommand "ssh -i /c/Users/steph/.ssh/smd/id_rsa"

# mac / linux
git config --global core.sshCommand "ssh -i ~/.ssh/smd/id_rsa"
```

### Micromamba
```bash
micromamba activate
micromamba shell init
micromamba create -n ollama-foundation python=3.13
micromamba activate ollama-foundation
pip install -r requirements.txt
```

### Ollama

```bash
# mac / linux
curl -fsSL https://ollama.com/install.sh | sh

# modeles utilisés
ollama pull gemma3:27b-cloud
ollama pull gemma4
ollama pull nomic-embed-text
ollama pull deepseek-r1:1.5b
ollama pull granite4.1:3b
ollama pull minimax-m2.7:cloud

# execution
export OLLAMA_HOST=http://localhost:11434/
export SSL_CERT_FILE=
python ollama-x.py
```

### LangChain

```bash
export OLLAMA_API_KEY="your-api-key"
export OLLAMA_HOST=https://api.ollama.com
python langchain-x.py
```

