class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y

class Rectangle:
    def __init__(self, point1, point2, *args):
        self.point1 = point1
        self.point2 = point2
        self.__sp = super().__new__(Point)
        self.__ep = super().__new__(Point)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep
        self.point1 = self.__sp
        self.point2 = self.__ep

    def get_coords(self):
        return self.point1, self.point2

    def draw(self):
        print(f'Прямоугольник с координатами: {self.get_coords()[0]} {self.get_coords()[1]}')

rect = Rectangle((0,0), (20,43))
