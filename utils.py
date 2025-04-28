import re

def read_file(filePath):
    dataLines = []
    with open(f"./data/{filePath}.txt", 'r', encoding="utf-8-sig") as file:
        for line in file:
            if len(line.strip()) == 0:
                continue
            dataLines.append(line.strip())       
    return dataLines

def read_characters_file(filePath):
    characters = []
    with open(f"./data/personnages-{filePath}.txt", 'r', encoding="utf-8-sig") as file:
        for line in file:
            if line.startswith("•"):
                continue

            character_name, town = line.strip().split(":", 1)
            characters.append((character_name.strip(), town.strip()))
            
    return characters;

def is_town_name(currentLine: str, nextLine: str):
    cleaned = currentLine.replace('-', '').replace(' ', '')
    townStatsPattern = r'^\(\d{5}\) - (\d+( \d+)*) hab\.$'
    return cleaned.isupper() and bool(re.match(townStatsPattern, nextLine))

def is_start_of_character(s: str):
    startOfCharacterPattern = r'^[A-ZÉÈÀÙÂÊÎÔÛÇ]+(?:\*|\s\(de\)|\sou\s[A-ZÉÈÀÙÂÊÎÔÛÇ]+)?(?:\sdit\s[A-ZÉÈÀÙÂÊÎÔÛÇ\-]+)?,\s[A-ZÉÈÀÙÂÊÎÔÛÇa-zéèàùâêîôûç\-]+(?:-[A-ZÉÈÀÙÂÊÎÔÛÇa-zéèàùâêîôûç]+)?\.$'
    return re.match(startOfCharacterPattern, s);

def extract_characters_info():
    characters = []

#def snipe_character_lines(data_lines, characters):
