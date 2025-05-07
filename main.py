import json
import pandas as pd
from typing import List
from characters import Character, extract_characters
from towns import Town, extract_towns
from mistral import extract_information_bio

def read_file(department):
    dataLines = []
    with open(f"./data/inputs/{department}/text.txt", 'r', encoding="utf-8-sig") as file:
        for line in file:
            if len(line.strip()) == 0:
                continue
            dataLines.append(line.strip())       
    return dataLines

def read_characters_file(department):
    characters = []
    with open(f"./data/inputs/{department}/characters.txt", 'r', encoding="utf-8-sig") as file:
        for line in file:
            if line.startswith("•"):
                continue

            character_name, town = line.strip().split(" - ", 1)
            characters.append((character_name.strip(), town.strip()))
            
    return characters

def main():
    file = "deux-sevres"
    data_lines = read_file(file)
    characters_index = read_characters_file(file)
    towns: List[Town] = extract_towns(data_lines, characters_index)
    
    characters: List[Character] = []
    for town in towns :
        print(town["name"])
        
        characters_partial = extract_characters(town["characters_text"], town["characters"], town["name"])
        for char in characters_partial:
            char["principal_place"] = town["name"] + " (" + town["postal_code"] + ")"
            characters.append(char)

    # verify the character extraction
    characters.sort(key=lambda char: char["family_name"])
    for char in characters:
        for char_i in characters_index:
            known_name = char_i[0].split()[0].replace(',', '')
            char_name = char["family_name"].split()[0].replace(',', '')
            if char_name == known_name:
                characters_index.remove(char_i)
    if len(characters_index) > 0:
        raise Exception("CHARACTERS REMAINING")

    # extract place_of_birth and place_of_death with LLM
    for char in characters:
        data = extract_information_bio(char)
        data_list = list(data.values())
        char["place_of_birth"] = data_list[0]
        if len(data_list) > 1:
            char["place_of_death"] = data_list[1]
    
    # export to json
    with open(f"data/outputs/{file}.json", "w", encoding="utf-8") as f:
        json.dump(characters, f, indent=4, ensure_ascii=False)

    # export to excel
        df = pd.DataFrame(characters)
        df.to_excel(f"data/outputs/{file}.xlsx", index=False)


if __name__ == "__main__":
    main()