from ollama import chat
from ollama import ChatResponse

def extract_information_bio(text):
    prompt = f"""
    Tu es un assistant qui lit une bibliographie de pionniers de la Nouvelle-France. Ton travail est d’extraire  les lieux et dates de naissance et/ou de déces mentionnés dans le text fournis. J'aimerai avoir l'information bien structuée en format JSON

    Texte :
    \"\"\"{text}\"\"\"

    """

    response: ChatResponse = chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}],
        format="json"
    )

    print(response.message.content)