def print_product_list(product_list):
    emoji = {
        'яблоко': '🍎', 'хлеб': '🍞', 'конфеты': '🍬', 'лимон': '🍋',
        'морковь': '🥕', 'огурец': '🥒', 'помидор': '🍅', 'яйцо': '🥚',
        'чеснок': '🧄', 'авокадо': '🥑', 'спички': '🥢', 'соль': '🧂',
        'филе говядины': '🥩', 'киви': '🥝', 'лук': '🧅', 'сыр': '🧀',
    }
    counts = {}
    for product in product_list:
        counts[product] = counts.get(product, 0) + 1
    for product, count in counts.items():
        print(f'{emoji.get(product, product)}: {count}')
