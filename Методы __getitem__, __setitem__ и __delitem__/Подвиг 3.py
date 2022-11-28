class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.liner_way = []

    def add_point(self, x, y, speed):
        self.liner_way.append([x,y,speed])

    def __getitem__(self, item):
        if isinstance(item, int) and 0 <= item <= len(self.liner_way)-1:
            return tuple(self.liner_way[item][:2]), self.liner_way[item][-1]
        else:
            raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key <= len(self.liner_way)-1:
            self.liner_way[key][-1] = value
        else:
            raise IndexError('некорректный индекс')




tr = Track(10, -5.4)

tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
print(tr[0])
coords, speed = tr[0]
print(coords, speed)
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

print(tr[2])
tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError