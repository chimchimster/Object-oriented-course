class Tuple(tuple):
    def __add__(self, other):
        return Tuple(tuple(self)+ tuple(other))

t = Tuple([1,2,3])
t3 = t + 'Python'
print(t3)