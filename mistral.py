import json
from ollama import chat
from ollama import ChatResponse

def extract_information_bio(text: str):
    prompt = f"""
        Tu es un assistant chargé de lire des biographies de pionniers de la Nouvelle-France. Ton travail consiste à extraire certaines informations mentionnées dans le texte fourni. Voici le format de réponse attendu :

        {{
            "lieu_naissance_ou_bapteme": "Nom du lieu",
            "lieu_deces_ou_inhumation": "Nom du lieu"
        }}

        TRÈS IMPORTANT: Si une information est introuvable/inconnue/ou non spécifiée, laisser une valeur vide

        Texte :
        \"\"\"{text}\"\"\"

    """

    response: ChatResponse = chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}],
        format="json"
    )

    data = json.loads(response.message.content)

    return data