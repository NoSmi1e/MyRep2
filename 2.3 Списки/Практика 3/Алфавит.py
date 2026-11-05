letters = []
for i in range(26):
    letter = chr(ord('a') + i)
    letters.append(letter * (i + 1))
print(letters)
