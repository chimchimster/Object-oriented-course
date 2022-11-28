class Money:
    type_money = None
    def __init__(self, value=0):
        self.__cb = None
        self.__volume = value

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, val):
        self.__cb = val

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, val):
        self.__volume = val

    def __check_volumes(self, other):
        if self.cb == None:
            raise ValueError("Неизвестен курс валют.")
        else:
            v1 = self.volume / self.cb.rates[self.type_money]
            v2 = other.volume / other.cb.rates[other.type_money]
            return v1, v2

    def __eq__(self, other):
        v1, v2 = self.__check_volumes(other)
        return abs(v1 - v2) < 0.1

    def __lt__(self, other):
        v1, v2 = self.__check_volumes(other)
        return v1 < v2

    def __le__(self, other):
        v1, v2 = self.__check_volumes(other)
        return v1 <= v2


class MoneyR(Money):
    type_money = 'rub'
class MoneyD(Money):
    type_money = 'dollar'
class MoneyE(Money):
    type_money = 'euro'

class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return

    @classmethod
    def register(cls, money):
        money.cb = cls




r = MoneyR(45000)
d = MoneyD(1500)

CentralBank.register(r)
CentralBank.register(d)

if r == d:
    print("неплохо")
else:
    print("нужно поднажать")