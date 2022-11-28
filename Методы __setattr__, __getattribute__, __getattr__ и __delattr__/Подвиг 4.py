class Shop:
    def __init__(self, title):
        self.title = title
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if len(self.goods) >= 1:
            self.goods.remove(product)

class Product:
    id = 0
    attrs_check_collection = {'id': int, 'name': str, 'weight': [int, float], 'price': (int, float)}

    def __new__(cls, *args, **kwargs):
        cls.id += 1
        return super().__new__(Product)

    def __init__(self, name, weight, price):
        self.id = Product.id
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in self.attrs_check_collection and \
                self.attrs_check_collection[key] == type(value) \
                or type(value) in self.attrs_check_collection[key] \
                and key in ('weight', 'price') and value > 0:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)

j = Product("Python ООП", 100, 1024)
del j.id
print(j.__dict__)

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")


j = Product("Python ООП", 100, 1024)
del j.id
print(j.__dict__)