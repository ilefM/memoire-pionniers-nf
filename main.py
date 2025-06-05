import json
import os
import pandas as pd
from typing import List
from characters import Character, extract_characters
from towns import Town, extract_towns
from mistral import extract_information_bio

# En attente de AI seulement 2: gironde, landes, lot-et-garonne, pyrenees-atlantiques, ariege, aveyron, haute-garonne, gers, lot, hautes-pyrenees, tarn, tarn-et-garonne

# En attente de AI 9: alpes-haute-provence, hautes-alpes, alpes-maritimes, bouches-du-rhone, var, vaucluse, aude, gard, herault, lazere, pyrenees-orientales

# En attente de AI 3: calvados, manche, orne, eure, seine-maritime,

# En attente de AI 10: loire-atlantique, maine-et-loire, mayenne, sarthe, vendee 

# En attente de AI 12: ain, ardeche, drome, isere

DEPARTMENT = "isere"

def read_file(department):
    dataLines = []
    with open(f"./data/inputs/{department}/{department}.txt", 'r', encoding="utf-8-sig") as file:
        for line in file:
            if len(line.strip()) == 0:
                continue
            dataLines.append(line.strip())       
    return dataLines

def read_characters_file(department):
    characters = []
    with open(f"./data/inputs/{department}/{department}-characters.txt", 'r', encoding="utf-8-sig") as file:
        for line in file:
            character_name, town = line.strip().split(" - ", 1)
            characters.append((character_name.strip(), town.split(",")[0].strip()))
            
    return characters

def main():
    data_lines = read_file(DEPARTMENT)
    characters_index = read_characters_file(DEPARTMENT)
    towns: List[Town] = extract_towns(data_lines, characters_index)
    
    characters: List[Character] = []
    for town in towns :
        print(town["name"])
        
        characters_partial = extract_characters(town["characters_text"], town["known_characters"], town["name"])
        for char in characters_partial:
            # data = extract_information_bio(char["bio"])
            # data_list = list(data.values())
            # char["birthplace"] = data_list[0]
            # if len(data_list) > 1:
            #     char["deathplace"] = data_list[1]
            char["mainplace"] = town["name"] + " (" + town["postcode"] + ")"
            town["characters"].append(char)
            characters.append(char)

    # verify the character extraction
    characters.sort(key=lambda char: char["lastname"])
    for char in characters:
        for char_i in characters_index:
            known_name = char_i[0].split()[0].replace(',', '')
            char_name = char["lastname"].split()[0].replace(',', '')
            if char_name == known_name:
                characters_index.remove(char_i)
    if len(characters_index) > 0:
        raise Exception("CHARACTERS REMAINING")
    

    path = os.path.join(os.getcwd(), './data/outputs', DEPARTMENT)
    os.makedirs(path, exist_ok=True)

    # export towns (with characters) to json
    towns_selected_properties = ["name", "postcode", "population", "description", "characters"]

    towns_filtered_properties = [
        {field: obj[field] for field in towns_selected_properties if field in obj}
        for obj in towns
    ]

    with open(f"./data/outputs/{DEPARTMENT}/{DEPARTMENT}-towns.json", "w", encoding="utf-8") as f:
        json.dump(towns_filtered_properties, f, indent=4, ensure_ascii=False)
    
    # export characters to json
    with open(f"./data/outputs/{DEPARTMENT}/{DEPARTMENT}-characters.json", "w", encoding="utf-8") as f:
        json.dump(characters, f, indent=4, ensure_ascii=False)

    # export characters to excel
    df = pd.DataFrame(characters)
    df.to_excel(f"./data/outputs/{DEPARTMENT}/{DEPARTMENT}.xlsx", index=False)


if __name__ == "__main__":
    main()