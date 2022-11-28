import sys
class DescrStr:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__ (self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_str(value)
        instance.__dict__[self.name] = value

    @classmethod
    def check_str(cls, value):
        if type(value) != str:
            raise TypeError('Неверный тип данных. Должен быть STR!')

class DescrInt:
    def __set_name__ (self, owner, name):
        self.name = '_' + name

    def __get__ (self, instance, owner):
        return getattr(instance, self.name)

    def __set__ (self, instance, value):
        self.check_int(value)
        instance.__dict__[self.name] = value

    @classmethod
    def check_int(cls, value):
        if type(value) != int:
            raise TypeError('Неверный тип данных. Должен быть INT!')

class Book:
    title = DescrStr()
    author = DescrStr()
    pages = DescrInt()

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Книга: {self.title}; {self.author}; {self.pages}'

book = Book(13, 'lsdkfm', 12)
print(book)

