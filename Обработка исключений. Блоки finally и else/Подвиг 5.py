class Point:
    def __init__(self, x=0, y=0):
        if x:
            self._x = x
            self._y = y
        else:
            self._x = 0
            self._y = 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

def func():
    pt = None
    a, b = input().split()
    try:
        a, b = int(a), int(b)
        pt = Point(a, b)
    except:
        try:
            a, b = float(a), float(b)
            pt = Point(a, b)
        except:
            try:
                pt = Point()
            except:
                pass
    finally:
        print(f'Point: x = {pt.x}, y = {pt.y}')

func()