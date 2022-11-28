class ListInteger(list):
    def __init__(self, l):
        super().__init__(l)

    def __check_type(self, item):
        if not isinstance(item, int):
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        self.__check_type(value)
        super().__setitem__(key, value)

    def append(self, item):
        self.__check_type(item)
        super().append(item)



s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError


