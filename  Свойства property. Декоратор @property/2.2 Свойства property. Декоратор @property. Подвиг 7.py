class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        self.x = x
        self.y = y


    @classmethod
    def __verif(cls, val):
        return type(val) in (int, float) and cls.MIN_COORD <= val <= cls.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new):
        if self.__verif(new):
            self.__x = new

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new):
        if self.__verif(new):
            self.__y = new

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y
