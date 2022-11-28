class DescrIntFloat:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_value(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_value(cls, value):
        if value > 0:
            return True
        else:
            raise ValueError("габаритные размеры должны быть положительными числами")

class Dimensions:
    a, b, c = DescrIntFloat(), DescrIntFloat(), DescrIntFloat()
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a,self.b,self.c))

string = input().split('; ')
print(string)
lst_dims = [x.split() for x in string]
for i in lst_dims:
    for j in i:
        if '.' in j:
            i[i.index(j)] = float(j)
        if j.isdigit():
            i[i.index(j)] = int(j)
lst_dims = [Dimensions(*x) for x in lst_dims]
lst_dims = sorted(lst_dims, key=hash)
print(lst_dims[0].a, lst_dims[1].a, lst_dims[2].a, lst_dims[3].a)