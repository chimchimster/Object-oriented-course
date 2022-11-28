class Record:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            self.__dict__[key] = val

    def __getitem__(self, item):
        if isinstance(item, int) and item > len(self.__dict__):
            raise IndexError('неверный индекс поля')
        i = 0
        for key in self.__dict__:
            if i == item:
                return self.__dict__[key]
            i += 1

    def __setitem__(self, key, value):
        if isinstance(key, int) and key > len(self.__dict__):
            raise IndexError('неверный индекс поля')
        self.__dict__[tuple(self.__dict__)[key]] = value

r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.__dict__)
print(r[1])
r[1] = 0
print(r[10])