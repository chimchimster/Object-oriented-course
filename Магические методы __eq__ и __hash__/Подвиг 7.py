import sys
class DescrStr:
    def __set_name__(self, owner, name):
        self.name = '_'  + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_value(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_value(cls, value):
        if type(value) == str:
            return True
        else:
            raise TypeError('not STR!')

class DescrInt:
    def __set_name__(self, owner, name):
        self.name = '_'  + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_value(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_value(cls, value):
        if type(value) == int:
            return True
        else:
            raise TypeError('not INT!')

class DataBase:
    path = DescrStr()

    def __init__(self, path):
        self.path = path
        self.dict_db = dict()

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        for key in self.dict_db.keys():
            if key.pk == pk:
                return key

class Record:
    fio = DescrStr()
    descr = DescrStr()
    old = DescrInt()
    START_INDEX = 0

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.START_INDEX
        Record.START_INDEX += 1

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        if hash(self) == hash(other):
            return True
        else:
            return False

lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in не менять!

db = DataBase('/path')
for i in lst_in:
    args = list(map(str.strip, i.split(';')))
    args[-1] = int(args[-1])
    db.write(Record(*args))

db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)
assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"