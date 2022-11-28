class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):
        self.tm = tm
        if self.__check_time(self.tm):
            self.__time = self.tm

    def get_time(self):
        return self.__time

    def __check_time(self, tm):
        self.tm = tm
        if type(self.tm) == (int) and 0 < self.tm < 100000:
            return True
        return False

clock = Clock()
clock.set_time(4530)
print(clock.get_time())