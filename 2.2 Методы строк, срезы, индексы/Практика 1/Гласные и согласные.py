text = input().lower()
vowels = "ауоыиэяюе"
consonants = "бвгджзйклмнпрстфхцчшщ"
vowel_count = 0
consonant_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1

print("Количество гласных букв равно", vowel_count)
print("Количество согласных букв равно", consonant_count)
