def uid_match(input_uid, extracted_uid):
    if len(input_uid) != len(extracted_uid):
        return False
    for i, j in zip(input_uid, extracted_uid):
        if i != j:
            return False
    return True
