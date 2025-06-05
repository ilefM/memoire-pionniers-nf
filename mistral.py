import json
from ollama import chat
from ollama import ChatResponse

# def extract_information_bio(text: str):
#     prompt = f"""
#         Tu es un assistant chargé de lire des biographies de pionniers de la Nouvelle-France. Ton travail consiste à extraire certaines informations mentionnées dans le texte fourni. Voici le format de réponse attendu :

#         {{
#             "lieu_naissance_ou_bapteme": "Nom du lieu",
#             "lieu_deces_ou_inhumation": "Nom du lieu"
#         }}

#         TRÈS IMPORTANT: Si une information est introuvable/inconnue/ou non spécifiée, laisser une valeur comme ceci: ""

#         Texte :
#         \"\"\"{text}\"\"\"

#     """

#     response: ChatResponse = chat(
#         model="mistral",
#         messages=[{"role": "user", "content": prompt}],
#         format="json"
#     )

#     data = json.loads(response.message.content)

#     return data

def extract_birthplace(text: str):
    prompt = f"""
        Tu es un assistant chargé de lire des biographies de pionniers de la Nouvelle-France. Ton travail consiste à extraire le lieu de naissance ou bapteme, PAS le lieu de mariage, du personnage mentionnée dans le texte fourni.

        TRÈS IMPORTANT: Si une information est introuvable/inconnue/ou non spécifiée dans le text, alors retourner une valeur vide (string vide)

        Texte :
        \"\"\"{text}\"\"\"

    """

    response: ChatResponse = chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}],
        format="json"
    )

    data = json.loads(response.message.content)

    values = list(data.values())

    if len(values) == 0:
        return ""
    
    value = values[0]

    if "Non spécifié" in value or "non spécifié" in value or "Inconnu" in value:
        return ""

    return values[0]


def extract_deathplace(text: str):
    prompt = f"""
        Tu es un assistant chargé de lire des biographies de pionniers de la Nouvelle-France. Ton travail consiste à extraire le lieu de mort, deces ou d'inhumation (PAS le lieu de mariage) du personnage mentionnée dans le texte fourni.

        TRÈS IMPORTANT: Si une information est introuvable/inconnue/ou non spécifiée dans le text, alors retourner une valeur vide (string vide)

        Texte :
        \"\"\"{text}\"\"\"

    """

    response: ChatResponse = chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}],
        format="json"
    )

    data = json.loads(response.message.content)

    values = list(data.values())

    if len(values) == 0:
        return ""
    
    value = values[0]

    if "Non spécifié" in value or "non spécifié" in value or "Inconnu" in value:
        return ""

    return values[0]