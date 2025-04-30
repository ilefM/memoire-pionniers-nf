import re


def extract_characters(characters_text, known_characters, name):
    extracted_characters = []
    character_bio = []
    characters_left = len(known_characters)

    bio_source_simple = re.compile(r"\. \(([A-ZÀ-Ý ]+([-&][A-ZÀ-Ý ]+)*)\)$")
    bio_source_reference = re.compile(r"\. \(([A-ZÀ-Ý0-9 ]+([-&][A-ZÀ-Ý0-9 ]+)*)\)$")
    bio_source_line = re.compile(r"^\(([A-ZÀ-Ý0-9 ]+([-&][A-ZÀ-Ý0-9 ]+)*)\)$")
    
    i = 0
    while i < len(characters_text):
        line = characters_text[i]
        character_bio.append(line)

        if i == len(characters_text) - 1:
            extracted_characters.append(character_bio[:])
            characters_left -= 1
            break

        elif (bio_source_simple.search(line) or
              bio_source_reference.search(line) or
              (bio_source_line.search(line) and line.startswith("(") and line.endswith(")"))):
            extracted_characters.append(character_bio[:])
            character_bio = []
            characters_left -= 1
        
        
        i += 1

    for char in extracted_characters:
        i = 0
        char_string = ""
        while i < len(char):
            if i == 0:
                char_string = char[0]
            elif char[i - 1].endswith("-"):
                char_string = char_string + char[i]
            else:
                char_string = char_string + " " + char[i]

            i += 1

    if characters_left != 0 or characters_left < 0:
        print(name)
        raise Exception("Characters extraction failed")

    return extracted_characters

