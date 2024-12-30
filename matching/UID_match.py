def uid_match(input_uid, extracted_uid):
    if len(input_uid) != len(extracted_uid):
        return 0
    for i, j in zip(input_uid, extracted_uid):
        if i != j:
            return 0
    return 100
