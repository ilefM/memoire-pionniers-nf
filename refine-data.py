# greff e, fill e, Lafl eur, fi ls, fi lle,

# references definition

import json
import csv
from typing import List, Tuple, TypedDict
import unicodedata

from characters import Character


class Town(TypedDict):
    name: str
    code_insee: str
    description: str
    position: Tuple[float, float]
    characters: List[Character]

towns_final: List[Town] = []

with open('code-insee-code-postal.json', 'r') as file:
            code_insees = json.load(file)

import unicodedata

def remove_accents(input_str):
    # Normalize the string to 'NFKD' form
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    # Filter out the combining characters (accents)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])



# def get_insee_code(dep, insees):
#     for town in dep:
#         data_town_name = town["name"].lower()
#         for insee in insees:
#             insee_town_name = insee[1].lower()
#             if data_town_name == insee_town_name:
#                 towns_final.append({
#                      "name": town["name"],
#                      "code_insee": insee[0],
#                      "description": town["description"],
#                      "position": ("", ""),
#                      "characters": town["characters"]
#                 })
                  

# def get_position():
#      for town in towns_final:
#           for commune in communes_france:
#                if town["code_insee"] == commune["code_insee"]:
#                     town["position"] = (commune["latitude_centre"], commune["longitude_centre"])
#                     town["url_villedereve"] = commune["url_villedereve"]
 
        
def get_position_and_insee(towns, dep):
    count = 0;
    for town in towns:
        town_final: Town = {
            "name": town["name"],
            "description": town["description"],
            "characters": town["characters"],
            "code_insee": "",
            "position": (0, 0),   
        }

        data_town_name = remove_accents(town["name"].lower()).replace("’", "'")
          
        for code_insee in code_insees:
            commune_name = code_insee["nom_comm"].lower()
            if data_town_name == commune_name and dep.upper() in code_insee["nom_dept"]:
                town_final["code_insee"] = code_insee["insee_com"]
                town_final["position"] = (code_insee["geo_point_2d"]["lat"], code_insee["geo_point_2d"]["lon"])
                count += 1

        towns_final.append(town_final)
    print(len(towns) - count)

        



if __name__ == "__main__":
    department = "deux-sevres"
    with open(f'data/outputs/{department}/{department}-towns.json', 'r') as file:
        towns = json.load(file)
    
    get_position_and_insee(towns, department)


    with open(f"./data/outputs/{department}/{department}-towns-final.json", "w", encoding="utf-8") as f:
        json.dump(towns_final, f, indent=4, ensure_ascii=False)
