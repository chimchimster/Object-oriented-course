class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

class TableValues:
    def __init__(self, rows=0, cols=0, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = tuple(tuple(Cell() for x in range(self.cols)) for x in range(self.rows))

    def __check_index_row(self, indx):
        if type(indx) != int and not(0 <= indx <= self.rows):
            raise IndexError('неверный индекс')

    def __check_index_col(self, indx):
        if type(indx) != int and not(0 <= indx <= self.cols):
            raise IndexError('неверный индекс')

    def __check_type_data(self, data):
        if type(data) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')

    def __getitem__(self, item):
        a, b = item
        self.__check_index_row(a)
        self.__check_index_col(b)
        return self.table[a][b].data

    def __setitem__(self, key, value):
        a, b = key
        self.__check_index_row(a)
        self.__check_index_col(b)
        self.__check_type_data(value)
        self.table[a][b].data = value

    def __iter__(self):
        for i in self.table:
            yield (d.data for d in i)

tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"