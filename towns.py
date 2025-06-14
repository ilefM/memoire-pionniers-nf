import re
from typing import List, TypedDict

from characters import Character

class Town(TypedDict):
    name: str
    postcode: str
    population: str
    description: str
    known_characters: List[str]
    characters_text: List[List[str]]
    characters: List[Character]

def get_characters_of_town(current_town: str, characters: List[str]):
    town_characters = []

    for character in characters:
        town_name = character[1].split(" - ")[-1]
        cleaned_town_name = re.sub(r"[^a-zA-ZÀ-ÿ]", "", town_name).upper()
        if character[1].upper() == current_town or cleaned_town_name == current_town:
            town_characters.append(character[0])
    return town_characters;

def match_characters_name(line, actual_name):
    first_word = line.split()[0].upper().replace("*", "").replace(",", "")
    actual_name = actual_name.split()[0].replace(",", "")
    if first_word == actual_name:
        return True
    return False

def is_town_name(currentLine: str, nextLine: str):
    cleaned = currentLine.replace('-', '').replace(' ', '')
    townStatsPattern1 = r'^\(\d{5}\)-(\d+( \d+)*) hab\.$'
    townStatsPattern2 = r'^\(\d+\D+\)-(\d+( \d+)*) hab\.$'
    townStatsPattern3 = r'^\(\d{5}\) - (\d+( \d+)*) hab\.$'
    townStatsPattern4 = r'^\(\d{5}\), (\d+( \d+)*) hab\.$'
    townStatsPattern5 = r'^\(\d{5}\), (\d+( \d+)*) [\w\-\'\s]+\.$'
    townStatsPattern6 = r'^\(\d{5}\) - (\d+( \d+)*) [\w\-\'\s]+\.$'
    townStatsPattern7 = r'^\(\d{5}\) – (\d+( \d+)*) hab\.$'
    return cleaned.isupper() and (bool(re.match(townStatsPattern1, nextLine)) or bool(re.match(townStatsPattern2, nextLine)) or bool(re.match(townStatsPattern3, nextLine)) or bool(re.match(townStatsPattern4, nextLine)) or bool(re.match(townStatsPattern5, nextLine)) or bool(re.match(townStatsPattern6, nextLine)) or bool(re.match(townStatsPattern7, nextLine)))

def extract_towns(data_lines, characters_index):
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
        if "," in town[1]:
            postal_code = town[1].split(",")[0].replace("(", "").replace(")", "").replace(" ", "")
            population = town[1].split(",")[1].strip()
        elif "-" in town[1]:
            postal_code = town[1].split("-")[0].replace("(", "").replace(")", "").replace(" ", "")
            population = town[1].split("-")[1]

        else:
            postal_code = town[1].split("–")[0].replace("(", "").replace(")", "").replace(" ", "")
            population = town[1].split("–")[1]

        description = ""
        current_town_characters = get_characters_of_town(name, characters_index)
        if len(current_town_characters) == 0:
            print(name)
            raise Exception("no characters found, verify the txt files")
        first_character = current_town_characters[0].split()[0].replace(",", "")

        
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

        towns.append({
            "name": name,
            "postcode": postal_code,
            "population": population,
            "description": description,
            "known_characters": current_town_characters,
            "characters_text": characters_text,
            "characters": []
         })
            
    return towns