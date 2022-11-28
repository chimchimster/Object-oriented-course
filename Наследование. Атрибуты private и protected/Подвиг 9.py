def class_log(lst):
    def cls_acceptor(cls):
        for name,  method in cls.__dict__.items():
            if callable(method):
                setattr(cls, name, filter_calls(name, lst))
        return cls
    return cls_acceptor

def filter_calls(name, lst):
    def wrapper(*args):
        lst.append(name)
        return None
    return wrapper

vector_log = []

@class_log(vector_log)
class Vector:

    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value



v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)
