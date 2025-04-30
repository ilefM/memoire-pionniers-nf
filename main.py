from typing import List
from characters import extract_characters
from towns import Town, extract_towns
from utils import read_characters_file, read_file
from mistral import extract_information_bio
    
def main():
    files = [
        "charente",
    ]

    for file in files:
        data_lines = read_file(file)
        characters = read_characters_file(file)
        towns: List[Town] = extract_towns(data_lines, characters)

        for town in towns :
            characters_text = town["characters_bio"]
            known_characters = town["characters"]
            extracted_characters = extract_characters(characters_text, known_characters, town["name"])

            for char in extracted_characters:
                extract_information_bio(char)

        # Export to json
        







if __name__ == "__main__":
    main()

# TODO:
#   AI to retreive data from character's bio
#   export to json for easy data access and manipulation  lieu : est la paroisse et la ville.
#   apres une ville le format peut etre comme ca : (33334) - 13 000 hab OU (10 communes) - 15 444 hab
#   export to excel file for viewing data
#   test script with other departements