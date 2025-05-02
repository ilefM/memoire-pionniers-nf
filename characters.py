import re
from typing import TypedDict, List

class Character(TypedDict):
    family_name: str
    first_name: str
    bio: str
    principal_place: str
    place_of_birth: str
    place_of_death: str

def extract_characters(characters_text, known_characters, name):
    extracted_characters = []
    characters_left = len(known_characters)

    bio_source_simple = re.compile(r"\. \(([A-ZÀ-Ý ]+([-&°.][A-ZÀ-Ý ]+)*)\)$")
    bio_source_reference = re.compile(r"\. \(([A-ZÀ-Ý0-9 ]+([-&°.][A-ZÀ-Ý0-9 ]+)*)\)$")
    bio_source_line = re.compile(r"^\(([A-ZÀ-Ý0-9 ]+([-&°.][A-ZÀ-Ý0-9 ]+)*)\)$")
    
    i = 0
    char_string = ""
    while i < len(characters_text):
        line = characters_text[i]
        if i == 0:
            char_string = line
        elif characters_text[i -1].endswith("-"):
            char_string = char_string + line
        else:
            char_string = char_string + " " + line

        if i == len(characters_text) - 1:
            extracted_characters.append(char_string)
            characters_left -= 1
            break

        elif (bio_source_simple.search(line) or
              bio_source_reference.search(line) or
              (bio_source_line.search(line) and line.startswith("(") and line.endswith(")"))):
            extracted_characters.append(char_string)
            char_string = ""
            characters_left -= 1
        
        i += 1

    if characters_left != 0 or characters_left < 0:
        print(name)
        raise Exception("Characters extraction failed")
    
    i = 0
    characters: List[Character] = []
    while i < len(known_characters):
        characters.append({
            "family_name": known_characters[i].split(",")[0],
            "first_name": known_characters[i].split(",")[1],
            "bio": extracted_characters[i]
        })
        i += 1

    return characters

