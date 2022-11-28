"""class TV_descriptorStr:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_str(value):
            setattr(instance, self.name, value)

    @classmethod
    def check_str(cls, string):
        return type(string) == str


class TV_descriptorNum:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_num(value):
            setattr(instance, self.name, value)

    @classmethod
    def check_num(cls, num):
        return type(num) in (int, float)"""

class TVProgram:
    def __init__(self, channel):
        self.channel = channel
        self.items = list()

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for i in self.items:
            if i.uid == indx:
                self.items.remove(i)


class Telecast:
    """id = TV_descriptorNum()
    name = TV_descriptorStr()
    duration = TV_descriptorNum()"""

    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        if self.check_num(value):
            self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if self.check_str(value):
            self.__id = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if self.check_num(value):
            self.__id = value

    @classmethod
    def check_str(cls, string):
        return type(string) == str

    @classmethod
    def check_num(cls, num):
        return type(num) in (int, float)

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
pr.remove_telecast(1)

for t in pr.items:
    print(f"{t.name}: {t.duration}")

print(pr.__dict__)