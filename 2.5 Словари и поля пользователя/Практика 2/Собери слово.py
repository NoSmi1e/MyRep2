from collections import Counter

def scrabble(letters, word):
    available = Counter(letters.lower())
    required = Counter(word.lower())
    return all(available[letter] >= count for letter, count in required.items())
