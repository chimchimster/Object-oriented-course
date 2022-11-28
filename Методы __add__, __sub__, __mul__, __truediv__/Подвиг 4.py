class NewList:
    def __init__(self, *args):
        self.lst = []
        if len(args) > 0:
            self.lst.append(*args)
            self.lst = self.lst[0].copy()

    def get_list(self):
        return self.lst

    @staticmethod
    def sub_lists(lst, other):
        lst_temp = other[:]
        if len(other) == 0:
            return lst
        return [x for x in lst if not NewList.check_type(x, lst_temp)]

    @staticmethod
    def check_type(value, lst):
        res = any(map(lambda x: type(value) == type(x) and value == x, lst))
        if res:
            lst.remove(value)
        return res

    def __sub__(self, other):
        if not isinstance(other, (NewList, list)):
            raise ArithmeticError('Операнды должны быть List/NewList')
        if isinstance(other, NewList):
            return NewList(self.sub_lists(self.get_list(), other.lst))
        if isinstance(other, list):
            return NewList(self.sub_lists(self.get_list(), other))

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError('Левый операнды должны быть NewList')
        return NewList(self.sub_lists(other, self.get_list()))




lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
print(type(res_2))
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print(res_1.get_list(), res_2.get_list(), res_3.get_list(), res_4.get_list())