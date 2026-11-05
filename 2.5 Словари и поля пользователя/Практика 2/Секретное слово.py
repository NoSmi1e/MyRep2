from collections import Counter

word = input()
counts = Counter(word)
letters = {}
for _ in range(int(input())):
    letter, frequency = input().split(': ')
    letters[int(frequency)] = letter
print(''.join(letters[counts[char]] for char in word))
