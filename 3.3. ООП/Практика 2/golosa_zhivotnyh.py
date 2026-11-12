class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Неизвестный звук'


class Cat(Animal):
    def speak(self):
        return 'Мяу'


class Dog(Animal):
    def speak(self):
        return 'Гав'


def collect_voices(animals):
    voices = []
    for animal in animals:
        voices.append(f'{animal.name}: {animal.speak()}')
    return voices
