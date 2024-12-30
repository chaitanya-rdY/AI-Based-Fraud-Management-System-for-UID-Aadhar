import re
from difflib import SequenceMatcher

def normalize_address(address):
    # Remove common terms and non-alphanumeric characters, normalize spaces
    common_terms = ["marg", "lane", "township"]
    address = address.lower()
    for term in common_terms:
        address = address.replace(term, "")
    address = re.sub(r'[^a-zA-Z0-9\s]', '', address)
    address = re.sub(r'\s+', ' ', address).strip()
    return address

def pincode_match(input_pincode, extracted_pincode):
    input_pincode = input_pincode.replace(" ", "")
    extracted_pincode = extracted_pincode.replace(" ", "")
    return 100 if input_pincode == extracted_pincode else 0

def field_match(input_field, extracted_field):
    if input_field == extracted_field:
        return 100
    else:
        return int(SequenceMatcher(None, input_field, extracted_field).ratio() * 100)

def address_match(input_address, extracted_address, cutoff=70):
    input_address = normalize_address(input_address)
    extracted_address = normalize_address(extracted_address)
    
    input_fields = input_address.split()
    extracted_fields = extracted_address.split()
    
    total_score = 0
    total_weight = 0
    
    for input_field in input_fields:
        best_score = 0
        for extracted_field in extracted_fields:
            score = field_match(input_field, extracted_field)
            if score > best_score:
                best_score = score
        total_score += best_score
        total_weight += 100
    
    final_score = (total_score / total_weight) * 100
    return final_score >= cutoff

def is_address_match(input_address, extracted_address, input_pincode, extracted_pincode, cutoff=70):
    if pincode_match(input_pincode, extracted_pincode) == 100:
        return address_match(input_address, extracted_address, cutoff)
    return False


##it returns the match true if total_sccore is greater than 70 percent otherwise false