class SoftList(list):
    def __init__(self, lst):
        super().__init__(lst)
        self.lst = lst

    def __getitem__(self, item):
        if not (-1 <= item < len(self)):
            return False
        else:
            return self.lst[item]

sl = SoftList("python")
print(sl[0], sl[-1], sl[6], sl[-7], end=' ')