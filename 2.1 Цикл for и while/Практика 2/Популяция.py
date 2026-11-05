m = float(input())
p = int(input())
n = int(input())

for day in range(1, n + 1):
    print(day, m)
    m *= 1 + p / 100
