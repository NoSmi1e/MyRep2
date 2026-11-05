n = int(input())

for _ in range(n):
    for column in range(3):
        print(n, end=" " if column < 2 else "\n")
