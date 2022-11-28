import random


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.__psw_chars = psw_chars
        self.__min_length = min_length
        self.__max_lenght = max_length

    def __call__(self, *args, **kwargs):
        s = ''
        if isinstance(self.__psw_chars, str):
            psw_length = random.randint(self.__min_length,self. __max_lenght)
            for i in range(psw_length):
                s += random.choice(self.__psw_chars)
        return s

rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)

lst_pass = [rnd() for i in range(3)]
print(lst_pass)

