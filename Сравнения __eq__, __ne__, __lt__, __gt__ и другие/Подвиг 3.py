class DescrInt:
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
            raise TypeError('Value type must be integer')

class DescrIntFloat:
    def __set_name__ (self, owner, name):
        self.name = '_' + name

    def __get__ (self, instance, owner):
        return getattr(instance, self.name)

    def __set__ (self, instance, value):
        if self.__check_type(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_type (cls, value):
        if type(value) in (int, float):
            return True
        else:
            raise TypeError('Value type must be integer or float')

class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.way = list()

    def add_track(self, tr):
        self.way.append(tr)

    def get_list(self):
        return tuple(self.way)

    def __len__(self):
        len_1 = ((self.way[0].x - self.start_x) ** 2 + (self.way[0].y - self.start_y) ** 2) ** 0.5
        return int(len_1 + sum(self.__get_length(i) for i in range(1, len(self.way))))

    def __get_length(self, i):
        return ((self.way[i-1].x - self.way[i].x) ** 2 + (self.way[i-1].y - self.way[i].y) ** 2) ** 0.5

    def __eq__(self, other):
        return len(self) == len(other)

    def __ne__(self, other):
        return len(self) != len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

class TrackLine:
    to_x = DescrIntFloat()
    to_y = DescrIntFloat()
    max_speed = DescrInt()

    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

    @property
    def x(self):
        return self.to_x

    @x.setter
    def x(self, value):
        self.to_x = value

    @property
    def y(self):
        return self.to_y

    @y.setter
    def y(self, value):
        self.to_y = value

track1, track2 = Track(0, 0), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
print(track1.way)
res_eq = track1 == track2

