class PolyLine:
    def __init__(self, start_coord, *args):
        self.start_coord = start_coord
        self.coords = [start_coord] + [*args]

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        if len(self.coords) > 0:
            self.coords.pop(indx)

    def get_coords(self):
        return list(self.coords)

pl = PolyLine((10,3), (10,4), (10,5))
print(pl.get_coords())
pl.remove_coord(1)
print(pl.get_coords())
print(pl.__dict__)