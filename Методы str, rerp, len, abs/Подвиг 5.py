class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def remove_obj(self, indx):
        obj = self.get_obj(indx)
        if not obj:
            return

        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p



    def get_obj(self, indx):
        count = 0
        h = self.head
        while indx != count:
            count += 1
            h = h.next
        return h

    def __iter__(self):
        h = self.head
        while h:
            yield h
            h = h.next

    def __len__(self):
        return self.check_len()

    def __call__(self, *args, **kwargs):
        return self.get_obj(args[0]).data

    def check_len(self):
        count = 0
        h = self.head
        while h:
            count += 1
            h = h.next
        return count

class ObjList:
    def __init__ (self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data (self):
        return self.__data

    @data.setter
    def data (self, value):
        self.__data = value

    @property
    def prev (self):
        return self.__prev

    @prev.setter
    def prev (self, value):
        self.__prev = value

    @property
    def next (self):
        return self.__next

    @next.setter
    def next (self, value):
        self.__next = value


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))

for i in linked_lst:
    print(i.data)
n = len(linked_lst)  # n = 3
print(n)
s = linked_lst(1) # s = Balakirev