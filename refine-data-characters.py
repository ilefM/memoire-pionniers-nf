import json


# references = [
#     "AN": "Archives Nationales, suivi du lieu, de la ville ou du service concerné.",
#     "ANOM": "Archives Nationales d’Outre-Mer, Aix-en-provence."
#     "AD24": "Archives Départementales, suivi du N° du département concerné. (24 : Dordogne)."
#     "AM Rouen": "Archives Municipales, suivi du nom de la ville concernée."
#     "BRH": "Bulletin de Recherches Historiques, Revue éditée par Pierre-Georges Roy."
#     "DBAQ": "Dictionnaire biographique des ancêtres québécois de 1608 à 1700, par M. Langlois."
#     "DBC": "Dictionnaire biographique du Canada, en ligne. Bibliothèque et Archives du Canada, Université Laval."
#     "DBCCF": "Dictionnaire biographique du clergé canadien-français, par J.B. Allaire."
#     "DGFC": "Dictionnaire généalogique des familles canadiennes, par C. Tanguay."
#     "DGFQ": "Dictionnaire généalogique des familles du Québec des origines à 1730, R. Jetté, Presse Univ de Montréal, 1983."
#     "FG": "Site Francogène, Généalogie des Français d’Amérique du Nord des origines à 1765, D. Beauregard."
#     "FO": "Fichier Origine, Fédération Québécoise des Sociétés de Généalogie, direction M. Fournier, Montréal, 2001."
#     "FS": "Fédération des Familles Souches."
#     "J.Y.Bronze": "Les morts de la Guerre de Sept Ans, presse de l’Université Laval, 2001."
#     "NR": "Normand Robert, Nos origines en France, Edition Archiv Histo, 1984, 13 volumes."
#     "PRDH": "Programme de recherche en démographie historique de l’Université de Montréal, 1966."
#     "YL": "Y. Landry, Les filles du Roy, Leméac, 1992."
#     "PM": "Projet Montcalm, Sociétés de Généalogie Canadienne-Française, direction M. Fournier, Montréal, 2008-9."
# ]


if __name__ == "__main__":
    department = "deux-sevres"
    with open(f'data/outputs/{department}/{department}-towns-final.json', 'r', encoding="utf-8") as file:
        towns = json.load(file)
    
    for town in towns:
        characters = town["characters"]

        for char in characters:
            char["bio"] = char["bio"].replace("(TO BE DELETED)", "").strip()
            

    with open(f"./data/outputs/{department}/{department}-towns-final.json", "w", encoding="utf-8") as f:
        json.dump(towns, f, indent=4, ensure_ascii=False)