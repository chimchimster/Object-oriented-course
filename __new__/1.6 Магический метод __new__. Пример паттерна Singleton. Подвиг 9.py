class Point:
    def __new__(cls, *args, **kwargs):
        return super().__new__(Point)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

pt = Point(10,11)
print(pt)
pt_clone = pt.clone()
print(pt_clone)