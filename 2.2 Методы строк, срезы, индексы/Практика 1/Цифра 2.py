text = input()

for char in text:
    if char.isdigit():
        print("Цифра")
        break
else:
    print("Цифр нет")
