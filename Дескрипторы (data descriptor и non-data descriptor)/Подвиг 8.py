class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.check_str(value):
            instance.__dict__[self.name] = value

    @classmethod
    def check_str(cls, string):
        return type(string) == str and 2 <= len(string) <= 50

class PriceValue:
    def __init__(self, max_value=10000):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.check_int_float(value):
            instance.__dict__[self.name] = value


    @classmethod
    def check_int_float(cls, number):
        return type(number) in (int, float) and 0 <= number <= 10000

class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        if hasattr(product, 'price') and hasattr(product, 'name'):
            self.goods.append(product)

    def remove_product(self, product):
        self.goods.pop(self.goods.index(product))

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    name = StringValue(min_length=2, max_length=50)
    price = PriceValue(max_value=10000)

shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")