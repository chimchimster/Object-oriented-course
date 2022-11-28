class Book:
    def __init__(self, title, author, year):
        if isinstance((title, author), str):
            self.title = title
            self.author = author
        if isinstance(year, int):
            self.year = year

class Lib:
    def __init__(self):
        self.book_list = list()

    def adding_into_list(self, obj):
        self.book_list.append(obj)

    def removing_into_list(self, obj):
        self.book_list.remove(obj)

    def removing_by_index_into_list(self, indx):
        self.book_list.pop(indx)

    def __add__(self, other):
        self.adding_into_list(other)
        return self

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Book):
            self.removing_into_list(other)
            return self
        elif isinstance(other, int):
            self.removing_by_index_into_list(other)
            return self

    def __isub__(self, other):
        return self - other

    def __len__(self):
        return len(self.book_list)

l = Lib()
b = Book('Dorian Grey', 'Scot', 1995)
l = l + b
l += b
l -= b
l -= 0
print(l.book_list)
