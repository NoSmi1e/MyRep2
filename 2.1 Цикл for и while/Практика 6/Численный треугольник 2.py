n = int(input())
current = 1

for row in range(1, n + 1):
    for column in range(row):
        if column > 0:
            print(" ", end="")
        print(current, end="")
        current += 1
    print()
