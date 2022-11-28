class Rect:
    def __init__(self, x, y, width, height):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float)) and width > 0 and height > 0):
            raise ValueError('некорректные координаты и параметры прямоугольника')

        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def is_collision(self, rect):
        x2, y2, height2, width2 = rect.x, rect.y, rect.height, rect.width

        coord_height1 = self.y + self.height
        coord_width1 = self.x + self.width

        coord_height2 = y2 + height2
        coord_width2 = x2 + width2

        if not (coord_width1 < x2 or coord_width2 < self.x or coord_height1 < y2 or coord_height2 < self.y):
            raise TypeError('прямоугольники пересекаются')


def is_collision(r1, r2):
    try:
        r1.is_collision(r2)
    except TypeError:
        return True
    return False

lst_rect = [
            Rect(0, 0, 5, 3),
            Rect(6, 0, 3, 5),
            Rect(3, 2, 4, 4),
            Rect(0, 8, 8, 1),
            ]

lst_not_collision = [lst_rect[i] for i in range(len(lst_rect)) if
                     not any(is_collision(lst_rect[i], lst_rect[j]) for j in range(len(lst_rect))
                     if i != j)]

print(lst_not_collision)