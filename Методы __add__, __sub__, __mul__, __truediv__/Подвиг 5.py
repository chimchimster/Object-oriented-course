class ListMath:
    def __init__(self, lst=None):
        self.lst = list()
        if lst:
            self.lst = self.check_values(lst)
        self.lst_math = self.lst.copy()

    @staticmethod
    def check_values(lst):
        return [x for x in lst if type(x) in (int, float)]

    @staticmethod
    def plus(lst, other):
        return [x + other for x in lst]

    @staticmethod
    def minus(lst, other):
        return [x - other for x in lst]

    @staticmethod
    def num_minus(lst, other):
        return [other - x for x in lst]

    @staticmethod
    def multipy(lst, other):
        return [x*other for x in lst]

    @staticmethod
    def divide(lst, other):
        return [x / other for x in lst]

    @staticmethod
    def num_divide(lst, other):
        return [other / x for x in lst]

    @staticmethod
    def plus_list(list1, list2):
        return [x + y for x, y in zip(list1, list2)] + (list1 if len(list1) >= len(list2) else list2)[(min(len(list1),len(list2))):]

    @staticmethod
    def minus_list(list1, list2):
        return [x - y for x, y in zip(list1, list2)] + (list1 if len(list1) >= len(list2) else list2)[(min(len(list1), len(list2))):]

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return ListMath(self.plus(self.lst_math, other))
        elif isinstance(other, ListMath):
            return ListMath(self.plus_list(self.lst_math, other.lst_math))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return ListMath(self.minus(self.lst_math, other))
        elif isinstance(other, ListMath):
            return ListMath(self.minus_list(self.lst_math, other.lst_math))

    def __rsub__(self, other):
        return ListMath(self.num_minus(self.lst_math, other))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return ListMath(self.multipy(self.lst_math, other))

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return ListMath(self.divide(self.lst_math, other))

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            return ListMath(self.num_divide(self.lst_math, other))

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"