class Cart:
    def __init__(self):
        self.goods = []

    def add(self,gd):
        self.gd = gd
        self.goods.append(self.gd)

    def remove(self, indx):
        self.indx = indx
        del self.goods[indx]

    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
cart.add(TV('Samsung', 13000))
cart.add(TV('Sony', 15000))
cart.add(Table('IKEA', 3288))
cart.add(Notebook('ASUS', 13300))
cart.add(Notebook('MAC', 34334))
cart.add(Cup('Cup', 1000))
print(cart.get_list())

