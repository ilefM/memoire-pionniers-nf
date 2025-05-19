import re
import copy
from typing import TypedDict, List

class Character(TypedDict):
    lastname: str
    firstname: str
    mainplace: str
    birthplace: str
    deathplace: str
    bio: str

def extract_characters(characters_text, known_characters, name):
    extracted_characters = []
    character_left = copy.deepcopy(known_characters)

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
            char_string = ""
        
        i += 1

    if character_left != []:
        raise Exception("Characters extraction failed")
    
    i = 0
    characters: List[Character] = []
    while i < len(known_characters):
        name = known_characters[i].split(",")
        characters.append({
            "lastname": name[0].strip(),
            "firstname": name[1].strip(),
            "bio": extracted_characters[i].strip()
        })
        i += 1

    return characters

