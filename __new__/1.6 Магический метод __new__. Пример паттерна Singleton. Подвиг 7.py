class SingletonFive:
    name = None
    counter = 0

    def __new__(cls, *args, **kwargs):
        if cls.counter < 5:
            cls.name = super().__new__(cls)
            cls.counter += 1
        return cls.name

    def __del__(self):
        return self.name

    def __init__(self, name):
        self.name = name



objs = [SingletonFive(str(n)) for n in range(10)]
for i in objs:
    print(i.name)