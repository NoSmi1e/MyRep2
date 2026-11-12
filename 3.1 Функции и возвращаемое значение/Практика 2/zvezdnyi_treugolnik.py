def draw_triangle(fill, base):
    middle = (base + 1) // 2

    for count in range(1, middle + 1):
        print(fill * count)

    for count in range(middle - 1, 0, -1):
        print(fill * count)
