class TriangleChecker:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if str in list(map(type, (self.a, self.b, self.c))) or any((self.a<0, self.b<0, self.c<0)):
            return 1
        if int(self.a) + int(self.b) > int(self.c) or int(self.a) + int(self.c) > int(self.b) or int(self.b) + int(self.c) > int(self.a):
            return 3
        return 2

a, b, c = map(int, input().split())

tr = TriangleChecker(a,b,c)
print(tr.is_triangle())
