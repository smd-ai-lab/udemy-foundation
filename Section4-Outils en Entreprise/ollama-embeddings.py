import ollama

# Générer des embeddings pour une ou plusieurs phrases
response = ollama.embed(
    model='nomic-embed-text',  # Modèle spécialisé pour les embeddings
    input=[
        'Le ciel est bleu.',
        "L'herbe est verte.",
        'Les pommes sont rouges.'
    ]
)

# Chaque embedding est un vecteur de nombres (généralement 768 ou 1536 dimensions)
for i, embedding in enumerate(response['embeddings']):
    print(f"Phrase {i+1}: vecteur de dimension {len(embedding)}")
    print(f"Premières valeurs: {embedding[:5]}...")