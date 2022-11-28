class StringDigit(str):
    def __init__(self, val):
        self.__check_for_digits(val)
        self.value = val


    def __check_for_digits(self, string):
        for i in string:
            if i.isalpha():
                raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        if isinstance(other, str):
            self.__check_for_digits(other)
        return StringDigit(self.value + other)

    def __radd__(self, other):
        if isinstance(other, str):
            self.__check_for_digits(other)
        return StringDigit(other + self.value)


sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
print(sd)
sd = "789" + sd # StringDigit: 789123456
print(sd)
sd = sd + "12f" # ValueError
print(sd)