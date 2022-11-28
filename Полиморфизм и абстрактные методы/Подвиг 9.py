class IntFloat:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__check_value(value)
        setattr(instance, self.name, value)

    @classmethod
    def __check_value(cls, val):
        if not isinstance(val, (int, float)):
            raise TypeError('координаты должны быть числами')

class Track:
    def __init__(self, *args):
        self.__points = list(args)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)

class PointTrack:
    x = IntFloat()
    y = IntFloat()

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.__class__.__name__}: {self.x}, {self.y}'


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)

print(tr.points)