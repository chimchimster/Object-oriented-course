class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        return int((abs(self.x1-self.x2)**2 + abs(self.y1 - self.y2)**2)**0.5)

    def __bool__(self):
        if len(self) < 1:
            return False
        else:
            return True

line = Line(0.5,0.5,0.3,0.3)
print(bool(line))