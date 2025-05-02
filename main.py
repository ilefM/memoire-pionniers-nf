import json
import pandas as pd
from typing import List
from characters import Character, extract_characters
from towns import Town, extract_towns
from utils import read_characters_file, read_file
from mistral import extract_information_bio

    
def main():
    files = [
        "charente",
    ]

    for file in files:
        data_lines = read_file(file)
        characters_index = read_characters_file(file)
        towns: List[Town] = extract_towns(data_lines, characters_index)

        characters: List[Character] = []

        for town in towns :
            characters_partial = extract_characters(town["characters_text"], town["characters"], town["name"])

            for char in characters_partial:
                # data = extract_information_bio(char)
                # data_list = list(data.values())
                # print(town["name"], data_lines)
                # char["place_of_birth"] = data_list[0]
                # char["place_of_death"] = data_list[1]
                char["principal_place"] = town["name"] + " (" + town["postal_code"] + ")"
                characters.append(char)
        
        # export to json
        with open("characters.json", "w", encoding="utf-8") as f:
            json.dump(characters, f, indent=4, ensure_ascii=False)

        # export to excel
        df = pd.DataFrame(characters)
        df.to_excel("characters.xlsx", index=False)
        
        


if __name__ == "__main__":
    main()

# TODO:
#   AI to retreive data from character's bio
#   export to json for easy data access and manipulation  lieu : est la paroisse et la ville.
#   apres une ville le format peut etre comme ca : (33334) - 13 000 hab OU (10 communes) - 15 444 hab
#   export to excel file for viewing data
#   test script with other departements