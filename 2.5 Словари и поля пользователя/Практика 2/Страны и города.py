cities = {}
for _ in range(int(input())):
    country, *names = input().split()
    for city in names:
        cities[city] = country
for _ in range(int(input())):
    print(cities[input()])
