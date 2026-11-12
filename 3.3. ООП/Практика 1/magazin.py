class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity=1):
        self.products.append((product, quantity))

    def total(self):
        total_price = 0
        for product, quantity in self.products:
            total_price += product.price * quantity
        return total_price

    def get_lines(self):
        lines = []
        for product, quantity in self.products:
            price = product.price * quantity
            lines.append(f'{product.name}: {product.price} x {quantity} = {price}')
        return lines


def print_receipt(cart):
    for line in cart.get_lines():
        print(line)
    print(f'Итого: {cart.total()}')
