from fuzzywuzzy import fuzz
import re

def name_match(input_name, extracted_name):
    def normalize(name):
        return re.sub(r'\s+', ' ', name.strip().lower())

    def exact_letter_match(name1, name2):
        return name1 == name2

    def abbreviated_match(name1, name2):
        parts1 = name1.split()
        parts2 = name2.split()
        if len(parts1) == len(parts2):
            return all(p1[0] == p2[0] for p1, p2 in zip(parts1, parts2))
        return False

    def ignore_middle_names(name1, name2):
        parts1 = name1.split()
        parts2 = name2.split()
        if len(parts1) == 2 and len(parts2) == 3:
            return parts1[0] == parts2[0] and parts1[1] == parts2[2]
        if len(parts1) == 3 and len(parts2) == 2:
            return parts1[0] == parts2[0] and parts1[2] == parts2[1]
        return False

    def match_any_part(name1, name2):
        parts1 = set(name1.split())
        parts2 = set(name2.split())
        return not parts1.isdisjoint(parts2)

    def circular_match(name1, name2):
        parts1 = set(name1.split())
        parts2 = set(name2.split())
        return parts1 == parts2

    def single_letter_abbreviation(name1, name2):
        parts1 = name1.split()
        parts2 = name2.split()
        if len(parts1) == len(parts2):
            return all(p1 == p2 or p1[0] == p2[0] for p1, p2 in zip(parts1, parts2))
        return False

    input_name = normalize(str(input_name))
    extracted_name = normalize(str(extracted_name))

    score = fuzz.ratio(input_name, extracted_name)

    if exact_letter_match(input_name, extracted_name):
        return True
    if abbreviated_match(input_name, extracted_name):
        return True
    if ignore_middle_names(input_name, extracted_name):
        return True
    if match_any_part(input_name, extracted_name):
        return True
    if circular_match(input_name, extracted_name):
        return True
    if single_letter_abbreviation(input_name, extracted_name):
        return True

    return False
