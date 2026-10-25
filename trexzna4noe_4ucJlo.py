number = int(input())

a = number // 100
b = (number // 10) % 10
c = number % 10

print("Сумма цифр =", a + b + c)
print("Произведение цифр =", a * b * c)
