class ItemAttrs:
    data_base = list()

    def __getitem__(self, item):
        return self.data_base[item]

    def __setitem__(self, key, value):
        self.data_base[key] = value

class Point(ItemAttrs):
    def __init__(self, *args):
        self.data_base = list(args)

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
print(pt[0])
print(x, y)