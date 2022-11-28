import random
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
classes = [Line, Rect, Ellipse]
elements = list()

for i in range(217):
    rand_class = random.choice(classes)
    elements.append(rand_class(random.randint(0,10),
                               random.randint(0,10),random.randint(0,10),random.randint(0,10)))
for j in range(len(elements)):
    if isinstance(elements[j], Line) == True:
        elements[j] = Line(0,0,0,0)
print(elements[0].__dict__)
print(elements)
