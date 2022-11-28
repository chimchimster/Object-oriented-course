class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i+1):
                yield self.lst[i][j]

    def __next__(self):
        for i in iter(self):
            return i



lst = [['x00'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32', 'x33']]

s = TriangleListIterator(lst)
print(s.lst)
print(next(s))
print(next(s))
for x in s:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)