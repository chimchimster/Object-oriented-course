class DescrIntFloat:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_value(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_value(cls, value):
        if value > 0 and type(value) in (int, float):
            return True
        else:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

class Triangle:
    a, b, c = DescrIntFloat(), DescrIntFloat(), DescrIntFloat()

    def __init__(self, a, b, c):
        if b + c > a and a + c > b and a + b > c:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = (self.a + self.b + self.c) / 2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"