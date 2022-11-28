class StringVal:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.check_str(value):
            instance.__dict__[self.name] = value

    @classmethod
    def check_str(cls, string):
        return type(string) == str

class NumberVal:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.check_str(value):
            instance.__dict__[self.name] = value

    @classmethod
    def check_str(cls, number):
        return type(number) in (int, float)


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = list()

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        total = 0
        for i in self.things:
            if hasattr(i, 'weight'):
                total += getattr(i, 'weight')
        return total

class Thing:
    name = StringVal()
    weight = NumberVal()

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага2", 100))
bag.add_thing(Thing("Бумага1", 100))
bag.add_thing(Thing("Бумага3", 100))
bag.add_thing(Thing("Бумага4", 100))
bag.add_thing(Thing("Бумага5", 100))
w = bag.get_total_weight()
print(w)
for t in bag.things:
    print(f"{t.name}: {t.weight}")


