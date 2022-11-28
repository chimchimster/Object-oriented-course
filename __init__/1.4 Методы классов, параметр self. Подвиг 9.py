import sys

lst_in = '1 Сергей 23 120000', '2 Максим 32 32323'


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for i in data:
            self.lst_data.append(dict(zip(self.FIELDS, i.split())))
        return self.lst_data

    
    def select(self, a, b):
        return self.lst_data[a:b+1]


db = DataBase()

print(db.insert(lst_in))

