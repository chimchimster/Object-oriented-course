class CheckInt:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_type(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_type(cls, value):
        if type(value) == int:
            return True
        else:
            raise ValueError('NOT INT!')


class CheckStr:
    def __set_name__ (self, owner, name):
        self.name = '_' + name

    def __get__ (self, instance, owner):
        return getattr(instance, self.name)

    def __set__ (self, instance, value):
        if self.__check_type(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_type (cls, value):
        if type(value) == str:
            return True
        else:
            raise ValueError('NOT STR!')

class CheckIntFloat:
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
            raise ValueError('NOT INT/FLOAT!')

class Person:
    fio = CheckStr()
    job = CheckStr()
    old = CheckInt()
    salary = CheckIntFloat()
    year_job = CheckInt()

    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.lst = [self.fio, self.job, self.old, self.salary, self.year_job]

    def __next__(self):
        for i in self.lst:
            return i

    def __iter__(self):
        return iter(self.lst)

    def __getitem__(self, item):
        if not item in range(5):
            raise IndexError('неверный индекс')
        return self.lst[item]

    def __setitem__(self, key, value):
        if not key in range(5):
            raise IndexError('неверный индекс')
        self.lst[key] = value

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
print(pers[4])
for v in pers:
    print(v)