class DescrStr:
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
            raise TypeError('Type must be int/float')

class Box:
    def __init__(self):
        self.space = list()

    def add_thing(self, obj):
        self.space.append(obj)

    def get_things(self):
        return self.space

    def __eq__(self, other):
        res1 = sorted(self.space, key=lambda x: x.mass)
        res2 = sorted(other.space, key=lambda x: x.mass)
        if res1 == res2:
            return True
        else:
            return False

class Thing:
    name = DescrStr()
    mass = DescrIntFloat()

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

    def __ne__(self, other):
        return self.name.lower() != other.name.lower() or self.mass != other.mass

    def __lt__(self, other):
        if self.name != other.name:
            return self.mass < other.mass
        else:
            return self.name < other.name

t1 = Thing('aa', 1)
t2 = Thing('aa', 1)
print(t1==t2)

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

#print(b1 == b2)


