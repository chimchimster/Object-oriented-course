class Money:
    def __init__(self, money):
        self.__money = money

    def set_money(self, money):
        self.money = money
        if self.__check_money(self.money):
            self.__money = self.money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.mn = mn
        self.set_money(self.__money + mn.get_money())

    def __check_money(self, mn):
        self.mn = mn
        if type(self.mn) == int and self.mn >= 0:
            return True
        return False

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()
m2 = mn_2.get_money()
print(m1, m2)