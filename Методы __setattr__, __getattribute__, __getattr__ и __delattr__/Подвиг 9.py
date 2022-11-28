"""class Desr_int_float:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_int_float(value):
            setattr(instance, self.name, value)

    @classmethod
    def check_int_float(cls, number):
        return type(number) in (int, float)

class ValidateNum:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def validate(self, num):
        if type(num) in (int, float) and self.MIN_DIMENSION <= num <= self.MAX_DIMENSION:
            return True
        return False

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        elif key in ('_Dimensions__c', '_Dimensions__a', '_Dimensions__b'):
            return object.__setattr__(self, key, value)

class Dimensions:
    a, b, c = Desr_int_float(validator=ValidateNum()), Desr_int_float(validator=ValidateNum()), Desr_int_float(validator=ValidateNum())

    def __init__(self, a, b, c):
        self.__a, self.__b, self.__c = a, b, c

    def __setattr__(self, key, value):
        return object.__setattr__(self, key, value)

d = Dimensions(10.5, 20.1, 30)
print(d.__dict__)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
print(a,b,c)
d.MAX_DIMENSION = 10  # исключение AttributeError"""

class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a, self.__b, self.__c = a, b, c

    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION+1):
            self.__a = value
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION+1):
            self.__b = value
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION+1):
            self.__c = value

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        return object.__setattr__(self, key, value)

d = Dimensions(10.5, 20.1, 30)
print(d.__dict__)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
print(a,b,c)
d.MAX_DIMENSION = 10  # исключение AttributeError