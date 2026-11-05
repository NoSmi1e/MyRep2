count = 0

while True:
    mark = int(input())
    if mark < 1 or mark > 5:
        break
    if mark == 5:
        count += 1

print(count)
