class MaxPooling:
    def __init__(self, step=(2,2), size=(2,2)):
        self.step = step
        self.size = size

    def __call__(self, *args, **kwargs):
        for i in range(len(args)):
            if len(args[i]) % 2 == 0 and len(args) % 2 == 0 and:
                for j in args[i]:
                    if type(j) in (int, float):
                        return True
            else:
                raise ValueError("Неверный формат для первого параметра matrix.")