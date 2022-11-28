from abc import ABC, abstractmethod

class StackInterface(ABC):
    @abstractmethod
    def push_back (self, obj):
        raise TypeError

    @abstractmethod
    def pop_back (self):
        raise TypeError

class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self._tail = None
        self._last = None
        self._pre_last = None

    def push_back (self, obj):
        if not self._top:
            self._top = obj
        else:
            self._tail.next = obj
        self._tail = obj

    def pop_back (self):
        if len(self) == 1:
            self._last = self._top
            self._top = self._tail = None
            return self._last
        if not self._top:
            return None
        else:
            self.find_last()
            self.find_pre_last()
        return self._last

    def find_last(self):
        h = self._top
        while h:
            self._last = h
            h = h.next

    def find_pre_last(self):
        h = self._top
        while h.next != self.find_last():
            self._pre_last = h
            h = h.next
        self._pre_last.next = None

    def find_length(self):
        h = self._top
        count = 0
        while h:
            count += 1
            h = h.next
        return count

    def __iter__(self):
        h = self._top
        while h:
            yield h
            h = h.next

    def __len__(self):
        return self.find_length()

class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @property
    def next (self):
        return self._next

    @next.setter
    def next (self, val):
        self._next = val


assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"
