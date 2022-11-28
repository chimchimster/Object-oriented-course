class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, c):
        if type(c) == str and 2 <= len(c) <= 100:
            self.__model = c


c = Car()
c.car = 'Toyota'
print(c.car)