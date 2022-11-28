class Vector:
    def __init__(self, *args):
        self.arguments = args

    def __add__(self, other):
        lst_temp = list()
        if len(self.arguments) != len(other.arguments):
            raise ArithmeticError('размерности векторов не совпадают')
        for i in range(len(self.arguments)):
            lst_temp.append(self.arguments[i] + other.arguments[i])
        return Vector(*lst_temp)

    def __iadd__(self, other):
        lst_temp = list()
        if not isinstance(other, Vector):
            for i in range(len(self.arguments)):
                lst_temp.append(self.arguments[i] + other)
        else:
            for i in range(len(self.arguments)):
                lst_temp.append(self.arguments[i] + other.arguments[i])
        return Vector(*lst_temp)

    def __sub__(self, other):
        lst_temp = list()
        if len(self.arguments) != len(other.arguments):
            raise ArithmeticError('размерности векторов не совпадают')
        for i in range(len(self.arguments)):
            lst_temp.append(self.arguments[i] - other.arguments[i])
        return Vector(*lst_temp)

    def __isub__(self, other):
        lst_temp = list()
        if not isinstance(other, Vector):
            for i in range(len(self.arguments)):
                lst_temp.append(self.arguments[i] - other)
        else:
            for i in range(len(self.arguments)):
                lst_temp.append(self.arguments[i] - other.arguments[i])
        return Vector(*lst_temp)

    def __mul__(self, other):
        lst_temp = list()
        if len(self.arguments) != len(other.arguments):
            raise ArithmeticError('размерности векторов не совпадают')
        for i in range(len(self.arguments)):
            lst_temp.append(self.arguments[i] * other.arguments[i])
        return Vector(*lst_temp)

    def __eq__(self, other):
        return self.arguments == other.arguments

    def __ne__(self, other):
        return self.arguments != other.arguments

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
v2 -= v1
print(v2.arguments)
print(v1!=v2)