class DescrIntFloat:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_type(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_type(cls, value):
        if type(value) in (int, float):
            return True
        else:
            raise TypeError('Type must be int/float')

class Rect:
    x = DescrIntFloat()
    y = DescrIntFloat()
    width = DescrIntFloat()
    height = DescrIntFloat()

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        print(self.x, self.y, self.height, self.width)

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __hash__(self):
        return hash((self.width, self.height))

r1 = Rect(10, 5, 1010, 50)
r2 = Rect(-10, 4, 100, 50)
print(r1 == r2)
h1, h2 = hash(r1), hash(r2)   # h1 == h2
print(h1,h2)