class Digit:
    def __init__(self, value):
        self.check_type(value)
        self.value = value

    def check_type(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError('значение не соответствует типу объекта')

class Integer(Digit):
    def __init__(self, value):
        super().__init__(value)

    def check_type(self, val):
        if not isinstance(val, int):
            raise TypeError('значение не соответствует типу объекта')

class Float(Digit):
    def __init__ (self, value):
        super().__init__(value)

    def check_type (self, val):
        if not isinstance(val, float):
            raise TypeError('значение не соответствует типу объекта')

class Positive(Digit):
    def __init__ (self, value):
        super().__init__(value)

    def check_type (self, val):
        if not val > 0:
            raise TypeError('значение не соответствует типу объекта')

class Negative(Digit):
    def __init__ (self, value):
        super().__init__(value)

    def check_type (self, val):
        if not val < 0:
            raise TypeError('значение не соответствует типу объекта')

class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)

    def check_type(self, val):
        Integer.check_type(self, val)
        Positive.check_type(self, val)

class FloatPositive(Float, Positive):
    def __init__ (self, value):
        super().__init__(value)

    def check_type(self, val):
        Float.check_type(self, val)
        Positive.check_type(self, val)

digits = [PrimeNumber(10),
          PrimeNumber(1),
          PrimeNumber(113),
          FloatPositive(1.1),
          FloatPositive(1.2),
          FloatPositive(1.3),
          FloatPositive(1.4),
          FloatPositive(1.5),]


lst_positive = list(filter(lambda x: isinstance(x, Integer), digits))
lst_float  = list(filter(lambda x: isinstance(x, Float), digits))
print(lst_positive, lst_float, end='\n')