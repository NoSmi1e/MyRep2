number = int(input())

first = number // 1000
second = number // 100 % 10
third = number // 10 % 10
fourth = number % 10

if first + fourth == second - third:
    print("ДА")
else:
    print("НЕТ")
