numbers = list(map(int, input().split()))
numbers.sort()
print(*numbers)
print(*numbers[::-1])
