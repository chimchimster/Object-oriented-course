class Thing:
    _id = 0

    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):
        self.name = name
        self.price = price
        Thing._id += 1
        self.id = Thing._id
        self.weight, self.dims, self.memory, self.frm = weight, dims, memory, frm

    def get_data(self):
        return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)


class Table(Thing):
    def __init__(self, name, price, weight=None, dims=None):
        super().__init__(name, price)
        self.weight, self.dims = weight, dims


class ElBook(Thing):
    def __init__(self, name, price, memory=None, frm=None):
        super().__init__(name, price)
        self.memory, self.frm = memory, frm

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())

