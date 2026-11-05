seen = set()
for number in map(int, input().split()):
    print('YES' if number in seen else 'NO')
    seen.add(number)
