class Translator:
        d = dict()
        def add(self, eng, rus):
                if eng not in self.d:
                        self.d[eng] = [rus]
                else:
                        self.d[eng].append(rus)
                                
        def remove(self,eng):
                del self.d[eng]

        def translate(self,eng):
                for key, val in self.d.items():
                        if eng == key:
                                return val

tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove('car')
tr.translate('go')
print(*tr.translate('go'))


