import json
from typing import List
import pandas as pd

from characters import Character


# Read the Excel file into a pandas DataFrame
df = pd.read_excel("./vienne-more-characters.xlsx", sheet_name=0)

# Convert each row to a dictionary and collect them in a list
objects_list = []
for _, row in df.iterrows():
        # Convert NaN values to None for better Python compatibility
        row_dict = row.where(pd.notnull(row), None).to_dict()
        objects_list.append(row_dict)

characters: List[Character] = []
for obj in objects_list:
        characters.append({
                "lastname": obj["NOM"],
                "firstname": obj["Prénom"],
                "birthplace": obj["Lieu baptème"],
                "deathplace": obj["Lieu décès ou inhumation"],
                "bio": obj ["Biographie CFQLMC + FO + CIEQ"]
        })

with open(f"./data/outputs/vienne-more-characters.json", "w", encoding="utf-8") as f:
    json.dump(characters, f, indent=4, ensure_ascii=False)