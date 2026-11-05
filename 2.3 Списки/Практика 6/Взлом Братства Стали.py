n = int(input()[1:])
for _ in range(n):
    line = input()
    print(line.split('#', 1)[0].rstrip())
