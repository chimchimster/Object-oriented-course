class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if (key in ['title', 'author'] and type(value) != str ) or (key in ['pages', 'year'] and type(value) not in (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)

book = Book('Python ООП', 'Сергей Балакирев',123,2022)
b = Book()
print(book.__dict__)

