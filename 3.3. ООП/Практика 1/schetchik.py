class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def get_value(self):
        return self.value
