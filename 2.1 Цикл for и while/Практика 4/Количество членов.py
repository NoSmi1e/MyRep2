count = 0

while True:
    word = input()
    if word == "стоп" or word == "хватит" or word == "достаточно":
        break
    count += 1

print(count)
