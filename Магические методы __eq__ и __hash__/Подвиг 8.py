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

class BookStudy:
    name = DescrStr()
    author = DescrStr()
    year = DescrInt()

    def __init__(self, name, author, year):
        self.name = name.lower()
        self.author = author.lower()
        self.year = year

    def __hash__(self):
        return hash((self.name, self.author))




lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]
new_list = []
for i in lst_in:
    args = list(map(str.strip, i.split(';')))
    args[-1] = int(args[-1])
    new_list.append(args)

lst_bs = [BookStudy(*x) for x in new_list]

lst_temp = list()
for i in lst_bs:
    lst_temp.append(hash(i))

result = {i: lst_temp.count(i) for i in lst_temp}

count = 0
for val in result.values():
   if val > 0:
       count += 1
