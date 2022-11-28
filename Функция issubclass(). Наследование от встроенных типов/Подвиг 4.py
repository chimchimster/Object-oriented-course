class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

class DictShop(dict):
    def __init__(self, d=None):
        if not d:
            d = {}
        if not isinstance(d, dict):
            raise TypeError('аргумент должен быть словарем')
        if len(d) == 0:
            super().__init__({})
        for key in d.keys():
            if not isinstance(key, Thing):
                raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__(d)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)

th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2
print(dict_things.__dict__)

for x in dict_things:
    print(x.name, x.price, x.weight, end='\n')
