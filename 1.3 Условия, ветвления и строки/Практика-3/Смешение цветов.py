color1 = input()
color2 = input()

colors = ("красный", "синий", "желтый")

if color1 not in colors or color2 not in colors:
    print("ошибка цвета")
elif color1 == color2:
    print(color1)
elif (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
    print("фиолетовый")
elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
    print("оранжевый")
else:
    print("зеленый")
