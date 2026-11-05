n = int(input())
divisors = []
for number in range(1, n + 1):
    if n % number == 0:
        divisors.append(number)
print(divisors)
