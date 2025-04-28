from ollama import chat
from ollama import ChatResponse

def extract_characters_paragraph(text):
    prompt = f"""
    Tu es un assistant qui lit un texte historique. Ton travail est d’extraire  les noms des personnages mentionnés ainsi que leur biographie. Pour chaque personnage le paragraph se termine toujours par un point suivi d'un code en majuscule entre parentheses puis un saut à la ligne. La premiere phrase d'un paragraphe represente le nom complet du personnage. Ensuite ce qui suit par la suite represente sa biographie.
    Format attendu (retourne uniquement une liste JSON):
    [
    {{
        "name": "nom au complet du personnage",
        "bio": "biographie du personnage"
    }}
    ]

    Texte :
    \"\"\"{text}\"\"\"
    """

    response: ChatResponse = chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}],
        format="json"
    )

    print(response.message.content)