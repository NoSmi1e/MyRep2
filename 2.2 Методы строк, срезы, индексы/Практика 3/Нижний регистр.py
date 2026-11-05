text = input()
count = 0

for char in text:
    if char.islower():
        count += 1

print(count)
