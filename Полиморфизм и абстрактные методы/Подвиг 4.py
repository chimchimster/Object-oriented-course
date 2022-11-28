class ShopInterface:
    def get_id (self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    instance_id = 0

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.__create_id()

    @classmethod
    def __create_id(cls):
        cls.instance_id += 1
        return cls.instance_id

    def get_id(self):
        return self.__id

s1 = ShopItem('a', 10, 100)
s2 = ShopItem('b', 11, 110)
s3 = ShopItem('c', 12, 120)
print(s1.get_id())
print(s2.get_id())
print(s3.get_id())

