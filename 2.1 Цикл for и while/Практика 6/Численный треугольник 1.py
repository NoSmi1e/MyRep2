n = int(input())

for row in range(1, n + 1):
    for _ in range(row):
        print(row, end="")
    print()
