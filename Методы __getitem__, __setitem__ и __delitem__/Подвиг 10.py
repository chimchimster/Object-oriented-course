class SparseTable:
    def __init__(self):
        self.cols = 0
        self.rows = 0
        self.cells = dict()

    def update_index(self):
        self.rows = max(key[0] for key in self.cells) + 1
        self.cols = max(key[1] for key in self.cells) + 1

    def add_data(self, row, col, data):
        self.cells[(row, col)] = data
        self.update_index()

    def remove_data(self, row, col):
        try:
            del self.cells[(row, col)]
            self.update_index()
        except KeyError:
            raise IndexError('ячейка с указанными индексами не существует')

    def __getitem__(self, item):
        r, c = item
        if (r, c) not in self.cells.keys():
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.cells[(r, c)].value

    def __setitem__(self, key, value):
        item = (key[0], key[1])

        if item not in self.cells:
            self.cells[item] = Cell(value)
            self.update_index()
        else:
            self.cells[item] = Cell(value)

class Cell:
    def __init__(self, value):
        self.value = value


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"

for x in range(st.rows):
    print()
    for y in range(st.cols):
        if (x, y) in st.cells.keys():
            print(st[x, y], end = " ")
        else:
            print(y, end = " ")