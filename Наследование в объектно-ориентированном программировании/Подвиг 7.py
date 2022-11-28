class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls._instance_base is None:
                cls._instance_base = super().__new__(cls)
            return cls._instance_base
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name if type(name) is str else None

game = Game('Howdy')
print(game.__dict__)



