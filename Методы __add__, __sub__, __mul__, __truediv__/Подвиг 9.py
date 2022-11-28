class DescrIntFloat:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if isinstance(value, (int, float)):
            instance.__dict__[self.name] = value
        else:
            raise TypeError('Value type must be int/float')

class Box3D:
    width = DescrIntFloat()
    height = DescrIntFloat()
    depth = DescrIntFloat()

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)

    def __mul__(self, other):
        return Box3D(self.width*other, self.height*other, self.depth*other)

    def __rmul__(self, other):
        return self*other

    def __sub__(self, other):
        return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)

    def __floordiv__(self, other):
        return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other):
        return Box3D(self.width % other, self.height % other, self.depth % other)

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box2 % 3
print(box.width, box.height, box.depth)