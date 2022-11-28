class DescrStr:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str:
            setattr(instance, self.name, value)
        else:
            raise TypeError('Value type must be str')


class DescrIntFloat:
    def __set_name__ (self, owner, name):
        self.name = '_' + name

    def __get__ (self, instance, owner):
        return getattr(instance, self.name)

    def __set__ (self, instance, value):
        if type(value) in (int, float):
            setattr(instance, self.name, value)
        else:
            raise TypeError('Value type must be int/float')

class Item:
    name = DescrStr()
    money = DescrIntFloat()

    def __init__(self, name, money):
        self.name = name
        self.money = money

    @staticmethod
    def summ_items(money1, money2):
        money1 += money2
        return money1

    def __add__(self, other):
        return self.summ_items(self.money, other)

    def __radd__(self, other):
        return self + other

class Budget:
    def __init__(self):
        self.budget = []

    def add_item(self, it):
        self.budget.append(it.money)

    def remove_item(self, indx):
        self.budget.pop(indx)

    def get_items(self):
        return self.budget

it1 = Item('name1', 10)
it2 = Item('name2', 15)
it3 = Item('name3', 20)
res = it1 + it2 + it3
print(res)

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
print(my_budget.budget)
# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x