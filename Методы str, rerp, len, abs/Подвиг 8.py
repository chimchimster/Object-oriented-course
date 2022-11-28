class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __len__(self):
        return self.clock1.get_time() - self.clock2.get_time()

    def __str__(self):
        difference = self.clock1.get_time() - self.clock2.get_time()
        h = difference // 3600
        m = (difference % 3600) // 60
        s = ((difference % 3600) // 60) % 60
        if self.clock1.get_time() < self.clock2.get_time():
            return f'00: 00: 00'
        elif h < 10:
            return f'0{h}: {m}: {s}'
        else:
            return f'{h}: {m}: {s}'

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours*3600 + self.minutes*60 + self.seconds

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt)