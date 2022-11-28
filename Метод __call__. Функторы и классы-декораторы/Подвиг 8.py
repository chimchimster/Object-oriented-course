class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, func, *args, **kwargs):
        lst_temp = list()
        res = func.split()
        for i in res:
            lst_temp.append(int(i))
        return lst_temp

@InputDigits
def input_dg(input):
    return input

res = input_dg(input())
print(res)