class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        if isinstance(n, StackObj) or n is None:
            self.__next = n

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data = d

class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        h = self.top
        if h is None:
            return
        while h.next != self.last:
            h = h.next
        if h:
            h.next = None
        ls = self.last
        self.last = h
        if self.last is None:
            self.top = None
        return ls

    def get_data(self):
        s = list()
        h = self.top
        while h:
            s.append(h.data)
            h = h.next
        return s

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()
print(res)