def convert_to_python_case(text):
    result = ''

    for index in range(len(text)):
        if text[index].isupper() and index != 0:
            result += '_'
        result += text[index].lower()

    return result
