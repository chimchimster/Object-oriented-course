class FloatValue:
    @classmethod
    def check_float(cls, number):
        if type(number) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, name):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_float(value)
        setattr(instance, self.name, value)

class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value

class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell() for i in range(M)] for j in range(N)]

count = 1.0
table = TableSheet(5,3)
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = count
        count += 1
print(table.cells)

