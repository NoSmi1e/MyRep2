number = int(input())

if 1000 <= number <= 9999 and (number % 7 == 0 or number % 17 == 0):
    print("YES")
else:
    print("NO")
