class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data_prop(self):
        return self.__data

    @data_prop.setter
    def data_prop(self, value):
        self.__data = value

    @property
    def next_prop(self):
        return self.__next

    @next_prop.setter
    def next_prop(self, value):
        self.__next = value

class Stack:
    def __init__(self):
        self.top = None
        self.tail = None
        self.head = None

    def show(self):
        tmp = self.top
        while tmp.next_prop is not None:
            print(tmp.data_prop, end = ' ')
            tmp = tmp.next_prop
        print(tmp.data_prop)

    def push_back(self, obj):
        if self.top == None:
            self.top = self.head = self.tail = obj
        if self.top:
            self.head = obj
            self.tail.next_prop = self.head
            self.head.next_prop = None
        self.tail = self.head

    def pop_back(self):
        if self.top == None:
            return
        if self.top:
            self.tail = self.head
            self.tail.next_prop = None
            self.head = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for x in other:
            self.push_back(StackObj(x))
        return self

h = StackObj('5')
print(h._StackObj__data) # 5
st = Stack()
st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st.push_back(StackObj('3'))
st.show() # 1 2 3
st = st + StackObj('4')
st += StackObj('5')
st.show() # 1 2 3 4 5
st = st * [str(i) for i in range(6, 9)]
st *= [str(i) for i in range(9, 12)]
st.show() # 1 2 3 4 5 6 7 8 9 10 11 12