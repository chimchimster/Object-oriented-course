class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.top = None
        self.__last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.__last.next = obj
        self.__last = obj

    def push_front(self, obj):
        if self.top is None:
            self.__last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __iter__(self):
        h = self.top
        while h:
            yield h
            h = h.next

    def __len__(self):
        return sum(1 for _ in self)

    def _get_obj(self, indx):
        self.__check_index(indx)

        for i, obj in enumerate(self):
            if i == indx:
                return obj

    def __check_index(self, indx):
        if type(indx) != int or not (0 <= indx <= len(self)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        return self._get_obj(item).data

    def __setitem__(self, key, value):
        self._get_obj(key).data = value

s = Stack()
obj1 = StackObj('Объект1')
obj2 = StackObj('Объект2')
obj3 = StackObj('Объект3')
obj4 = StackObj('Объект4')
s.push_front(obj1)
s.push_front(obj2)
s.push_front(obj3)
s.push_front(obj4)
print(s.__dict__)
print(len(s))
for obj in s:
    print(obj.data)
