import csv
import json

def csv_to_json(csv_file_path: str, json_file_path: str):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
csv_to_json('data/inputs/communes-france-2025.csv', 'communes-france-2025.json')