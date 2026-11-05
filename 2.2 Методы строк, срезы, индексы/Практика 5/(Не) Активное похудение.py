day = int(input())
weight = float(input())

target = round(100 - 0.2 * day, 1)

if weight <= target:
    print("Все идет по плану")
else:
    print("Что-то пошло не так")

print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {target} кг")
