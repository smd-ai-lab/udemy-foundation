from langchain_ollama import ChatOllama


# Ollama
model_ollama = ChatOllama(model="granite4.1:30b", temperature=0.7)
reponse = model_ollama.invoke("Bonjour le monde !")

print(reponse.content)

""" content="Bonjour ! Comment puis-je vous aider aujourd'hui ?" 
additional_kwargs={} 
response_metadata={'model': 'granite4.1:30b', 'created_at': '2026-05-14T08:55:58.164358Z', 'done': True, 'done_reason': 'stop', 'total_duration': 556380250, 'load_duration': 58608334, 'prompt_eval_count': 12, 'prompt_eval_duration': 54376416, 'eval_count': 12, 'eval_duration': 438831334, 'logprobs': None, 'model_name': 'granite4.1:30b', 'model_provider': 'ollama'}
id='lc_run--019e25b3-23a6-75b1-bacb-02399e691472-0'
tool_calls=[]
invalid_tool_calls=[]
usage_metadata={'input_tokens': 12, 'output_tokens': 12, 'total_tokens': 24} """
