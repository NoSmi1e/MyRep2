n = int(input())

for number in range(1, n + 1):
    print(number, end="")
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            print("+", end="")
    print()
