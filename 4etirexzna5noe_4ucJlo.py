number = int(input())

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

print("Цифра тысяч =", thousands)
print("Цифра сотен =", hundreds)
print("Цифра десятков =", tens)
print("Цифра единиц =", units)
