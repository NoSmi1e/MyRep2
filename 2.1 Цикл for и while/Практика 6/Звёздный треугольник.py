n = int(input())
middle = (n + 1) // 2

for row in range(1, n + 1):
    count = row if row <= middle else n - row + 1
    for _ in range(count):
        print("*", end="")
    print()
