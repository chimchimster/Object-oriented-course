class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    def __abs__(self):
        return (self.__real*self.__real + self.__img*self.__img)**0.5

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if self.check_type(value):
            self.__real = value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if self.check_type(value):
            self.__img = value
        else:
            raise ValueError("Неверный тип данных.")

    @staticmethod
    def check_type(value):
        if type(value) in (int, float):
            return True

cmp = Complex(real=7, img=8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)
