class Ellipse:
    def __init__(self, *kwargs):
        self.flag_existis = False
        if len(kwargs) > 0:
            self.x1 = kwargs[0]
            self.y1 = kwargs[1]
            self.x2 = kwargs[2]
            self.y2 = kwargs[3]
            self.flag_existis = True

    def __bool__(self):
        if self.flag_existis:
            return True
        return False

    def get_coords(self):
        if self.__bool__() == True:
            return (self.x1, self.y1, self.x2, self.y2)
        else:
            raise AttributeError('нет координат для извлечения')

lst_geom = [Ellipse() for x in range(2)] + [Ellipse(1,1,2,2) for j in range(2)]
for i in lst_geom:
    if bool(i) == True:
        i.get_coords()