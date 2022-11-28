class Animal:
    def __init__(self, name, old):
        self.name = name if type(name) is str else None
        self.old = old if type(old) is int else None

class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color if type(color) is str else None
        self.weight = weight if weight > 0 and type(weight) in (int, float) else None

    def get_info(self):
        return f'{self.name}: {self.old}, {self.color}, {self.weight}'

class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed if type(breed) is str else None
        self.size = size if type(size) is tuple and len(size) == 2 else None
        self.height, self.weight = self.size

    def get_info(self):
        return f'{self.name}: {self.old}, {self.breed}, {self.height}, {self.weight}'


c = Cat('Murka', 10, 'white',10)
d = Dog('Bars', 10, 'Sheeper', (10, 14))
print(c.get_info())
print(d.get_info())