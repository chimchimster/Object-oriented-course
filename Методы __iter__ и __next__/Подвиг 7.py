class IterColumn:
    def __init__(self, lst, column=0):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for i in range(len(self.lst)):
                yield self.lst[i][self.column]

lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

s = IterColumn(lst,2)
for x in s:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)
