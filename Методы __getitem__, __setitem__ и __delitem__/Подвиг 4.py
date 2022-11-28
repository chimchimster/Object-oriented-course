class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.arr = [0] * self.max_length

    def __getitem__(self, item):
        if not isinstance(item, int) and 0 < item >= self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')
        return self.arr[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int) and 0 < key >= self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')
        if self.__check_cell(value):
            self.arr[key] = value

    def __str__(self):
        return ' '.join(map(str, self.arr))

    @classmethod
    def __check_cell(cls, value):
        if type(value) == int:
            return True
        else:
            raise ValueError('должно быть целое число')

class Integer:
    def __init__(self, start_value):
        self.start_value = start_value

    @property
    def value(self):
        return self.start_value

    @value.setter
    def value(self, val):
        if self.__check_type(val):
            self.start_value = val

    @staticmethod
    def __check_type(value):
        if type(value) == int:
            return True
        else:
            raise ValueError('должно быть целое число')


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
print(ar_int)
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
print(ar_int)

