parts = input().split('.')
valid = len(parts) == 4 and all(
    part.isascii() and part.isdecimal() and 0 <= int(part) <= 255
    for part in parts
)
print('ДА' if valid else 'НЕТ')
