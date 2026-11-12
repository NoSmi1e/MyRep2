class Wallet:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self._balance += amount
        return True

    def spend(self, amount):
        if amount <= 0 or amount > self._balance:
            return False
        self._balance -= amount
        return True
