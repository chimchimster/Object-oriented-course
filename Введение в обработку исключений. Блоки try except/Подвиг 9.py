class Triangle:
    def __init__(self, a, b, c):
        self.__check_val(a, b, c)
        self.__check_triangle(a, b, c)
        self._a = a
        self._b = b
        self._c = c

    def __check_val(self, a, b, c):
        if type(a) not in (int, float) or type(b) not in (int, float) or type(c) not in (int, float) or\
            a < 0 or b < 0 or c < 0:
            raise TypeError('стороны треугольника должны быть положительными числами')

    def __check_triangle(self, a, b, c):
        if (a > b + c) or (b > a + c) or (c > a + b):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

def filter_triangle(x):
    if len(x) != 3:
        return
    a, b, c = x
    try:
        return Triangle(a, b, c)
    except:
        return

input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = list(filter(lambda x: x is not None, map(lambda x: filter_triangle(x), input_data)))
print(lst_tr)