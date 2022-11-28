import time

class Mechanical:
    date = None

    def __init__(self, date):
        if self.validate_float(date):
            self.date = date

    @property
    def get_init_date(self):
        return self.date

    @classmethod
    def settin_local_date(cls):
        cls.date = cls.get_init_date

    @classmethod
    def gettin_local_date(cls):
        return cls.date

    @staticmethod
    def validate_float(number):
        return type(number) == float and number > 0

    def __setattr__(self, key, value):
        if self.date == None:
            return object.__setattr__(self, key, value)
        else:
            return

class Aragon(Mechanical):
    pass

class Calcium(Mechanical):
    pass

class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, filter):
        if self.slot_1 == None and slot_num == 1 and filter.__class__ == Mechanical:
            self.slot_1 = filter
        if self.slot_2 == None and slot_num == 2 and filter.__class__ == Aragon:
            self.slot_2 = filter
        if self.slot_3 == None and slot_num == 3 and filter.__class__ == Calcium:
            self.slot_3 = filter
        else:
            return False

    def remove_filter(self, slot_num):
        if self.slot_1 != None and slot_num == 1:
            self.slot_1 = None
        if self.slot_2 != None and slot_num == 2:
            self.slot_2 = None
        if self.slot_3 != None and slot_num == 3:
            self.slot_3 = None

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        if None not in self.get_filters():
            if None not in (self.slot_1.date, self.slot_2.date, self.slot_3.date):
                mech = time.time() - self.slot_1.date
                arg = time.time() - self.slot_2.date
                cal = time.time() - self.slot_3.date
                if mech <= self.MAX_DATE_FILTER and arg <= self.MAX_DATE_FILTER and cal <= self.MAX_DATE_FILTER:
                    return True
            return False
        return False

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
print(w)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
print(my_water.add_filter(2, Calcium(time.time()))) # добавление в "чужой" слот также невозможно
print(my_water.add_filter(1, Mechanical(time.time())))