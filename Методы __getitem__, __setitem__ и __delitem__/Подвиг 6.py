class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.__countobj = 0

    def push(self, obj):
        last = self[self.__countobj - 1] if self.__countobj > 0 else None

        if last:
            last.next = obj

        if self.top is None:
            self.top = obj

        self.__countobj += 1

    def pop(self):
        if self.__countobj == 0:
            return None

        last = self[self.__countobj - 1]

        if self.__countobj == 1:
            self.top = None
        else:
            self[self.__countobj - 2].next = None

        self.__countobj -= 1
        return last

    def __check_index(self, indx):
        if type(indx) != int or not (0 <= indx < self.__countobj):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)

        count = 0
        h = self.top
        while h and count < item:
            h = h.next
            count += 1

        return h

    def __setitem__(self, key, value):
        self.__check_index(key)

        h = self[key]
        prev = self[key-1] if key > 0 else None

        value.next = h.next
        if prev:
            prev.next = value




