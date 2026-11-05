from collections import Counter

def letters(text):
    return Counter(char for char in text.lower() if char.isalpha())

print('YES' if letters(input()) == letters(input()) else 'NO')
