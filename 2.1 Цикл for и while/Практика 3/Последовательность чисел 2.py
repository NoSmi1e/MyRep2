m = int(input())
n = int(input())

for number in range(m, n + 1):
    if number % 17 == 0 or number % 10 == 9 or number % 15 == 0:
        print(number)
