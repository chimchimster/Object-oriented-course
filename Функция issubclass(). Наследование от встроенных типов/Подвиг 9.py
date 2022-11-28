class IteratorAttrs:
    step = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.step += 1
        if self.step < len(self.__dict__)-1:
            return tuple(self.__dict__.items())[self.step]
        raise StopIteration

class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone('Nokia', (10,20), 256)

for attr, value in phone:
    print(attr, value)