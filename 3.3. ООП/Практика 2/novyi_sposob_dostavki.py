from zakaz_i_dostavka import Order


class FixedDelivery:
    def __init__(self, fee):
        self.fee = fee

    def calculate(self, subtotal):
        return self.fee
