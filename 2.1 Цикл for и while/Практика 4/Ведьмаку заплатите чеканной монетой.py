amount = int(input())
coins = 0

while amount > 0:
    if amount >= 25:
        coins += amount // 25
        amount %= 25
    elif amount >= 10:
        coins += amount // 10
        amount %= 10
    elif amount >= 5:
        coins += amount // 5
        amount %= 5
    else:
        coins += amount
        amount = 0

print(coins)
