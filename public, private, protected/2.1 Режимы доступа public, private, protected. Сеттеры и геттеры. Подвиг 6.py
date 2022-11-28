class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_author(self, author):
        self.author = author
        self.__author = self.author

    def set_title(self, title):
        self.title = title
        self.__title = self.title

    def set_price(self, price):
        self.price = price
        self.__price = self.price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

