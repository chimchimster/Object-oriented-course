class Clock:
    __DAY = 86400

    def __init__(self, seconds):
        if not isinstance(seconds, (int, Clock)):
            raise TypeError('Только int/Clock')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.get_formated(h)}:{self.get_formated(m)}:{self.get_formated(s)}'

    @classmethod
    def get_formated(cls, x):
        return str(x).rjust(2, '0')

    @staticmethod
    def check_for_type(value):
        if not isinstance(value, (int, Clock)):
            raise TypeError('Неверный тип данных')
        else:
            temp_other = value
            if isinstance(value, Clock):
                temp_other = temp_other.seconds
        return temp_other

    def __add__(self, other):
        return Clock(self.seconds + self.check_for_type(other))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.seconds += self.check_for_type(other)
        return self

    def __sub__(self, other):
        return Clock(self.seconds -self.check_for_type(other))

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        self.seconds -= self.check_for_type(other)
        return self

    def __mul__(self, other):
        return Clock(self.seconds * self.check_for_type(other))

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.seconds *= self.check_for_type(other)
        return self

    def __truediv__(self, other):
        return Clock(self.seconds / self.check_for_type(other))

    def __rtruediv__ (self, other):
        return self / other

    def __itruediv__ (self, other):
        self.seconds /= self.check_for_type(other)
        return self

c1 = Clock(1000)
c2 = Clock(2000)
c1 = 199*c1

print(c1.get_time())