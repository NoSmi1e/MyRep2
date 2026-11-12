class Pickup:
    def calculate(self, subtotal):
        return 0


class CourierDelivery:
    def calculate(self, subtotal):
        if subtotal < 1000:
            return 200
        return 0


class Order:
    def __init__(self, delivery):
        self.delivery = delivery
        self.prices = []

    def add_item(self, price):
        self.prices.append(price)

    def subtotal(self):
        return sum(self.prices)

    def total(self):
        if not self.prices:
            return 0
        subtotal = self.subtotal()
        return subtotal + self.delivery.calculate(subtotal)

    def set_delivery(self, delivery):
        self.delivery = delivery
