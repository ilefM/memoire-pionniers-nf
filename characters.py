import re
import copy
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
    character_left = copy.deepcopy(known_characters)
    nb_characters_left = len(known_characters)

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
            character_left.remove(character_left[0])
            nb_characters_left -= 1
            break

        elif (bio_source_simple.search(line) or
              bio_source_reference.search(line) or
              (bio_source_line.search(line) and line.startswith("(") and line.endswith(")"))):
            extracted_characters.append(char_string)
            next_line = characters_text[i + 1].split(" ")[0].replace("*", " ").replace(",", "").upper().strip()

            for char in character_left:
                char_name = char.split(" ")[0].replace(",", "").strip()
                if next_line == char_name:
                    character_left.remove(char)
                    break;
            nb_characters_left -= 1
            char_string = ""
        
        i += 1

    if nb_characters_left != 0:
        raise Exception("Characters extraction failed")
    
    i = 0
    characters: List[Character] = []
    while i < len(known_characters):
        characters.append({
            "family_name": known_characters[i].split(",")[0].strip(),
            "first_name": known_characters[i].split(",")[1].strip(),
            "bio": extracted_characters[i].strip()
        })
        i += 1

    return characters

