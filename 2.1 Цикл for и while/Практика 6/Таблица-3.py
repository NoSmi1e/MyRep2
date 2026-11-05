n = int(input())

for number in range(1, n + 1):
    for second in range(1, 10):
        print(f"{number} + {second} = {number + second}")
    if number != n:
        print()
