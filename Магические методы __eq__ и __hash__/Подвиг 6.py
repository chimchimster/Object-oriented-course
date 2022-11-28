import sys

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
            raise TypeError('not STR!')


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
            raise TypeError('not INT/FLOAT!')

class ShopItem:
    name = DescrStr()
    weight = DescrIntFloat()
    price = DescrIntFloat()

    def __init__(self, name, weight, price):
        self.name = name.lower()
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        v1 = [self.name, self.weight, self.price]
        v2 = [other.name, other.weight, other.price]
        return v1 == v2

    def __hash__(self):
        return hash((self.name, self.weight, self.price))

"""
s1 = ShopItem('Системный блок', 1500, 75890.56)
s2 = ShopItem('Монитор Samsung', 2000, 34000)
s3 = ShopItem('Клавиатура', 200.44, 545)
s4 = ShopItem('Монитор Samsung', 2000, 34000)
"""

lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']
lst_temp = [x.split(': ') for x in lst_in]
lst_temp = [[x[0], x[1].split(' ')[0], x[1].split(' ')[1]] for x in lst_temp]
for i in lst_temp:
    for j in i:
        if '.' in j:
            i[i.index(j)] = float(j)
        if j.isdigit():
            i[i.index(j)] = int(j)
lst_temp = [ShopItem(*x) for x in lst_temp]
shop_items = {}
for i in lst_temp:
    c = 1
    if i not in shop_items:
        shop_items[i] = [i, c]
    else:
        c += 1
        shop_items[i] = [i, c]
print(lst_temp)
print(shop_items)
