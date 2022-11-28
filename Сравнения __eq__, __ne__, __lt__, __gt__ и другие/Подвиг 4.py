class DescrStr:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    @classmethod
    def __check_type(cls, value):
        if type(value) == str:
            return True
        else:
            raise TypeError('Value type must be string')

class DescrIntFloat:
    def __set_name__ (self, owner, name):
        self.name = '_' + name

    def __get__ (self, instance, owner):
        return getattr(instance, self.name)

    def __set__ (self, instance, value):
        setattr(instance, self.name, value)

    @classmethod
    def __check_type(cls, value):
        if type(value) in (int, float):
            return True
        else:
            raise TypeError('Value type must be floating/integer')

class DescrDim:
    def __set_name__ (self, owner, name):
        self.name = '_' + name

    def __get__ (self, instance, owner):
        return getattr(instance, self.name)

    def __set__ (self, instance, value):
        setattr(instance, self.name, value)

    @classmethod
    def __check_type (cls, value):
        if type(value) == Dimensions:
            return True
        else:
            raise TypeError('Value type must be Dimensions')

class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def volume(self):
        return self.__a + self.__b + self.__c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION):
            self.__c = value

    def __eq__(self, other):
        return self == other

    def __gt__(self, other):
        return self.volume() > other

    def __ge__(self, other):
        return self.volume() >= other

    def __lt__(self, other):
        return self.volume() < other

    def __le__(self, other):
        return self.volume() <= other

class ShopItem:
    name = DescrStr()
    price = DescrIntFloat()
    dim = DescrDim()

    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim

    def volume(self):
        return self.dim


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)), ShopItem('зонт', 500.24, Dimensions(10, 20, 50)), ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)), ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume())
assert len(lst_shop) == 4, "число элементов в lst_shop не равно 4"

lst_sp = []
lst_sp.append(ShopItem('кеды', 1024, Dimensions(40, 30, 120)))
lst_sp.append(ShopItem('зонт', 500.24, Dimensions(10, 20, 50)))
lst_sp.append(ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)))
lst_sp.append(ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)))

lst_sp_sorted = ['зонт', 'кеды', 'табуретка', 'холодильник']
s = [x.name for x in lst_shop_sorted]
assert lst_sp_sorted == s, "список lst_shop_sorted сформирован неверно"

d1 = Dimensions(40, 30, 120)
d2 = Dimensions(40, 30, 120)
d3 = Dimensions(30, 20, 100)
assert d1 <= d2, "неверно отработал оператор <="
assert d3 <= d2, "неверно отработал оператор <="
assert d3 < d2, "неверно отработал оператор <"

d2.a = 10
d2.b = 10
d2.c = 10
assert d2 < d1, "неверно отработал оператор < после изменения объема через объекты-свойства a, b, c"