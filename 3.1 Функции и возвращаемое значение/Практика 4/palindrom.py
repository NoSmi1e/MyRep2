def is_palindrome(text):
    cleaned_text = ''
    text = text.lower()

    for char in text:
        if char not in ' ,.!?-':
            cleaned_text += char

    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False
