class Animal:
    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @property
    def kind(self):
        return self.__kind

    @property
    def old(self):
        return self.__old

animals = [Animal('Васька', 'дворовый кот', 5),
           Animal('Рекс', 'немецкая овчарка', 5),
           Animal('Кеша', 'попугай', 3)]