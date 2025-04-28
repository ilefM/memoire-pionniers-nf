from typing import List, TypedDict
from utils import is_town_name
import re

class Town(TypedDict):
    name: str
    postal_code: str
    population: str
    description: str
    characters: List[str]
    characters_text: List[str]
    charaters_bio: List[List[str]]


def get_characters_of_town(current_town: str, characters: List[str]):
    town_characters = []
    for character in characters:
        if character[1].upper() == current_town or character[1].upper() == current_town.split("-")[0]:
            town_characters.append(character[0])
    return town_characters;

#def is_end_of_description(current_line: str, characters: List[str]):
    # uppercase_line = current_line.upper()
    # upper_case_splitted = uppercase_line.split()[:2]
    # first_two_words = " ".join(upper_case_splitted).replace("*", "")
    # first_words_alt = re.sub(r"\s*\([^)]*\)", "", first_two_words).strip()
    # first_word = upper_case_splitted[0].replace("*", "")
    # for character in characters:
    #     if first_two_words in character.upper() or first_words_alt in character.upper():
    #         return True
    #     if first_word in character.split()[0]:
    #         return True
    # return False

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

        
        
        i = 0
        characters_bio = []
        bio = []
        while i < len(characters_text):
            bio.append(characters_text[i])
            if re.search(r'\.\s\([A-Z-]+\)', characters_text[i]):
                characters_bio.append(bio)
                bio = []
            elif i + 1 < len(characters_text) and re.search(r'\.\s\([A-Z-]*$', characters_text[i]) and re.match(r'^[A-Z-]*\)', characters_text[i+1]):
                bio.append(characters_text[i + 1])
                characters_bio.append(bio)
                bio = []
            i += 1


        towns.append({
            "name": name,
            "postal_code": postal_code,
            "population": population,
            "description": description,
            "characters": current_town_characters,
            "characters_text": characters_text,
            "characters_bio": characters_bio
         })
    
    # for town in towns:
    #     i = 0
    #     textarr = town["town_text"]
    #     text = ""
        
    #     while i < len(textarr):
    #         if i > 0 and textarr[i - 1].endswith("-"):
    #             text = text + textarr[i]
    #         elif i == 0:
    #             text = textarr[i]
    #         else:
    #             text = text + " " + textarr[i]
    #         i += 1
        
    #     town["town_text"] = text

            # name = data_lines[i].upper()
            # postal_code = data_lines[i + 1].split("-")[0].replace("(", "").replace(")", "").replace(" ", "");
            # population = data_lines[i + 1].split("-")[1]
            
            # # Extract all the text related to the current town (town description and characters)
            # text = []
            # for j in range(i + 2, len(data_lines)):
            #     if len(data_lines) - (j + 1) > 0 and is_town_name(data_lines[j], data_lines[j + 1]):
            #         i = j
            #         break;
            #     text.append(data_lines[j])
            
            # current_town_characters = get_characters_of_town(name, characters)

            # # Get town description
            # description = []
            # for line in text:
            #     if is_end_of_description(line, current_town_characters):
            #         break;
            #     description.append(line)     

                
            # town = {
            #     "name": name,
            #     "postal_code": postal_code,
            #     "population": population,
            #     "description": description,
            # }
            
    return towns