def print_products(*args):
    count = 0

    for product in args:
        if isinstance(product, str) and product != '':
            count += 1
            print(f'{count}) {product}')

    if count == 0:
        print('Нет продуктов')
