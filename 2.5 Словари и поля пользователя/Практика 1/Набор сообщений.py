keys = {'1': '.,?!:', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ', '0': ' '}
presses = {char: key * (index + 1) for key, chars in keys.items() for index, char in enumerate(chars)}
print(''.join(presses.get(char, '') for char in input().upper()))
