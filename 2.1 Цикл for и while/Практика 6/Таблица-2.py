n = int(input())

for row in range(1, n + 1):
    for column in range(5):
        print(row, end=" " if column < 4 else "\n")
