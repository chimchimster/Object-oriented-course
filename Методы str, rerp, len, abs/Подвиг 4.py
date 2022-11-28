class WordString:
    def __init__(self, string=''):
        self.__string = string

    def __len__(self):
        return len(self.string.split())

    def __call__(self, *args, **kwargs):
        for i in range(len(self.string.split())):
            if i == args[0]:
                return self.string.split()[args[0]]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")