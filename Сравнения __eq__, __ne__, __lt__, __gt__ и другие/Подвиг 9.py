class DesrcStr:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_type(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_type(cls, value):
        if type(value) == str:
            return True
        else:
            raise TypeError('Type must be str')


class DesrcIntFloat:
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
            raise TypeError('Type must be int/float')

class Body:
    name = DesrcStr()
    ro = DesrcIntFloat()
    volume = DesrcIntFloat()

    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.ro * self.volume == other
        return self.ro * self.volume == other.ro * other.volume

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.ro * self.volume > other
        return self.ro * self.volume > other.ro * other.volume

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.ro * self.volume < other
        return self.ro * self.volume < other.ro * other.volume

body1 = Body('1st', 10, 2)
body2 = Body('1nd', 10, 2)
print(body1==20)
print(body1 > body2)




