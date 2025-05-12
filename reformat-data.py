import json
import pandas as pd
from typing import List, TypedDict
from characters import Character
from towns import Town


department = "deux-sevres"

class NewCharacter(TypedDict):
    lastname: str
    firstname: str
    mainplace: str
    birthplace: str
    deathplace: str
    bio: str

class NewTown(TypedDict):
    name: str
    postcode: str
    population: str
    description: str
    characters: List[NewCharacter]

def reformat_towns_json():
    towns: List[Town] = []

    with open(f'./data/outputs/{department}/{department}-towns.json', 'r', encoding="utf-8") as file:
        towns = json.load(file)

    new_towns: List[NewTown] = []

    for town in towns:
        new_characters: List[NewCharacter] = []
        for char in town["characters"]:
            new_characters.append(
                {
                    "lastname": char["last_name"],
                    "firstname": char["first_name"],
                    "mainplace": char.get("main_place", ""),
                    "birthplace": char.get("birthplace", ""),
                    "deathplace": char.get("deathplace", ""),
                    "bio": char["bio"], 
                }
            )
        new_towns.append(
            {
                "name": town["name"],
                "postcode": town["postcode"],
                "population": town["population"].strip(),
                "description": town["description"],
                "characters": new_characters
            }
        )

    with open(f"./data/outputs/{department}/{department}-towns.json", "w", encoding="utf-8") as f:
        json.dump(new_towns, f, indent=4, ensure_ascii=False)

def reformat_characters_json_and_excel():
    characters: List[Character] = []

    with open(f'./data/outputs/{department}/{department}-characters.json', 'r', encoding="utf-8") as file:
        characters = json.load(file)

    new_characters: List[NewCharacter] = []
    for char in characters:
        new_characters.append({
            "lastname": char["last_name"],
            "firstname": char["first_name"],
            "mainplace": char.get("main_place", ""),
            "birthplace": char.get("birthplace", ""),
            "deathplace": char.get("deathplace", ""),
            "bio": char["bio"],
        })
        
    with open(f"./data/outputs/{department}/{department}-characters.json", "w", encoding="utf-8") as f:
        json.dump(new_characters, f, indent=4, ensure_ascii=False)


    df = pd.DataFrame(new_characters)
    df.to_excel(f'data/outputs/{department}/{department}.xlsx', index=False)

if __name__ == "__main__":
    reformat_towns_json()
    reformat_characters_json_and_excel()