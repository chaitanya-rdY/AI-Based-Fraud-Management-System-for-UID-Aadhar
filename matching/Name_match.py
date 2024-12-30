import re

def name_match(input_name, extracted_name):
    def normalize(name):
        #replaces the spaces with a single space
        return re.sub(r'\s+', ' ', name.strip().lower())

    def exact_letter_match(name1, name2):
        #checking the names are equal or not
        return name1 == name2

    def abbreviated_names(name1, name2):
        parts1 = name1.split()
        parts2 = name2.split()
        if len(parts1) == len(parts2):
            for p1, p2 in zip(parts1, parts2):
                if len(p1) == 1 or len(p2) == 1:
                    if p1[0] != p2[0]:
                        return False
                else:
                    if p1 != p2:
                        return False
            return True
        return False

    def ignoring_middle_names(name1, name2):
        parts1 = name1.split()
        parts2 = name2.split()
        if len(parts1) > len(parts2):
            parts1 = [p for p in parts1 if p in parts2]
        else:
            parts2 = [p for p in parts2 if p in parts1]
        return parts1 == parts2

    def matching_any_part(name1, name2):
        parts1 = set(name1.split())
        parts2 = set(name2.split())
        return not parts1.isdisjoint(parts2)

    def circular_matching(name1, name2):
        parts1 = set(name1.split())
        parts2 = set(name2.split())
        return parts1 == parts2

    input_name = normalize(input_name)
    extracted_name = normalize(extracted_name)

    score = 0

    if exact_letter_match(input_name, extracted_name):
        score += 5
    if abbreviated_names(input_name, extracted_name):
        score += 4
    if ignoring_middle_names(input_name, extracted_name):
        score += 3
    if matching_any_part(input_name, extracted_name):
        score += 2
    if circular_matching(input_name, extracted_name):
        score += 1

    return (score/15)*100

# Example usage
input_name = "John A. Doe"
extracted_name = "John Doe"
print(name_match(input_name, extracted_name))  # Output: score based on matching criteria
