def transform(text):
    result = {}
    for index, char in enumerate(text):
        result.setdefault(char, set()).add(index)
    return result
