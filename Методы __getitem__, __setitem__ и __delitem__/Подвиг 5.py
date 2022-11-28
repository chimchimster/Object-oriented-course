class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_type(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_type(cls, value):
        if type(value) == int:
            return True
        else:
            raise ValueError('возможны только целочисленные значения')


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

    @property
    def value_(self):
        return self.value

    @value_.setter
    def value_(self, val):
        self.value = val

class TableValues:
    cols = IntegerValue()
    rows = IntegerValue()
    def __init__(self, cols, rows, cell=None):
        self.cols = cols
        self.rows = rows
        self.cell = cell
        if not self.check_for_cell_type(self.cell):
            raise ValueError('параметр cell не указан')
        else:
            self.cells = tuple(tuple(self.cell() for _ in range(self.rows)) for _ in range(self.cols))
            self.cells_list = list(list(self.cell() for _ in range(self.rows)) for _ in range(self.cols))
    @classmethod
    def check_for_cell_type(cls, val):
        if val is None:
            return False
        else:
            return True

    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value_

    def __setitem__(self, key, value):
        self.cells_list[key[0]][key[1]].value_ = value
        self.cells = tuple(tuple(i) for i in self.cells_list)



table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10

print(table.cells)
# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()

