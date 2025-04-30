from typing import List, TypedDict
from utils import is_town_name
import re

class Town(TypedDict):
    name: str
    postal_code: str
    population: str
    description: str
    characters: List[str]
    characters_bio: list[list[str]]

def get_characters_of_town(current_town: str, characters: List[str]):
    town_characters = []
    for character in characters:
        if character[1].upper() == current_town or character[1].upper() == current_town.split("-")[0]:
            town_characters.append(character[0])
    return town_characters;

def match_characters_name(line, actual_name):
    first_word = line.split()[0].upper().replace("*", "").replace(",", "")
    actual_name = actual_name.split()[0].replace(",", "")
    if first_word == actual_name:
        return True
    return False



def extract_towns(data_lines, characters):
    towns_texts = []
    current_town = []
    i = 0
    while i < len(data_lines):
        if i > 0 and len(data_lines) - (i + 1) > 0 and is_town_name(data_lines[i], data_lines[i + 1]):
            towns_texts.append(current_town)
            current_town = []
        current_town.append(data_lines[i])
        i += 1
    towns_texts.append(current_town)

    towns: List[Town] = []
    for town in towns_texts:
        name = town[0]
        postal_code = town[1].split("-")[0].replace("(", "").replace(")", "").replace(" ", "")
        population = town[1].split("-")[1]
        description = ""
        current_town_characters = get_characters_of_town(name, characters)
        if len(current_town_characters) == 0:
            print(name)
            raise Exception("no characters found, verify the txt files")
        first_character = current_town_characters[0].split()[0].replace(",", "");

        
        i = 2
        characters_text = []
        while i < len(town):
            first_word = town[i].split()[0].replace("*", "").replace(",", "")
            if first_word == first_character:
                characters_text = town[i:]
                break
            elif town[i - 1].endswith("-"):
                description = description + town[i]
            elif i == 2:
                description = town[i]
            else:
                description = description + " " + town[i]
            i += 1


        # i = 0
        # all_characters_bio = []
        # character_bio = []
        # characters_left = len(current_town_characters)

        # # Regex patterns
        # bio_source_simple = re.compile(r"\. \([A-Z ]+-[A-Z ]+\)$")
        # bio_source_reference = re.compile(r"\. \([A-Z0-9 ]+-[A-Z0-9 ]+\)$")
        # bio_source_line = re.compile(r"^\([A-Z0-9 \-]+\)$")

        # while i < len(characters_text):
        #     if i == 1:
        #         print("jere")
        #     line = characters_text[i]
        #     character_bio.append(line)

            
        #     if (bio_source_simple.match(line) or 
        #         bio_source_reference.match(line) or 
        #         bio_source_line.fullmatch(line)):
                
        #         characters_left -= 1
        #         all_characters_bio.append(character_bio[:])
        #         character_bio = []

        #     if characters_left == 0 and i != len(characters_text) - 1:
        #         raise Exception("Error extracting characters: extra lines found")

        #     i += 1

        # if len(current_town_characters) != len(all_characters_bio):
        #     print(name)
        # characters_string = ""
        # i = 0
        # while i < len(characters_text):
        #     if i == 0:
        #         characters_string = characters_text[0]
        #     elif characters_text[i - 1].endswith("-"):
        #         characters_string = characters_string + characters_text[i]
        #     else:
        #         characters_string = characters_string + " " + characters_text[i]
        #     i += 1

        towns.append({
            "name": name,
            "postal_code": postal_code,
            "population": population,
            "description": description,
            "characters": current_town_characters,
            "characters_bio": characters_text,
         })
            
    return towns