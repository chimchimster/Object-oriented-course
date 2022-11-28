import random

class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.pole = self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self._is_human_win = False
        self._is_computer_win = False
        self._is_draw = False

    def __check_index(self, indx):
        r, c = indx
        if not r in range(3) or not c in range(3):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_index(item)

        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_index(key)

        r, c = key
        self.pole[r][c].value = value
        if self.check_winner_end(self.HUMAN_X):
            self.is_human_win = True
        elif self.check_winner_end(self.COMPUTER_O):
            self.is_computer_win = True


    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self._is_human_win = False
        self._is_computer_win = False
        self._is_draw = False

    def show(self):
        for row in self.pole:
            for el in row:
                print(el.value, end= ' ')
            print()

    def __bool__(self):
        if not self._is_human_win and not self._is_computer_win and not self._is_draw:
            return True
        else:
            return False

    def human_go(self):
        human_to_go = list(map(int, input('Введите 2 числа: ').split()))
        while True:
            if self.pole[human_to_go[0]][human_to_go[1]].value == 0:
                self.pole[human_to_go[0]][human_to_go[1]].value = self.HUMAN_X
                break
            else:
                print('Клетка уже занята!')
                human_to_go = list(map(int, input('Введите 2 числа: ').split()))

    def computer_go(self):
        comp_to_go = [random.randint(0,2), random.randint(0,2)]
        while True:
            if self.pole[comp_to_go[0]][comp_to_go[1]].value == 0:
                self.pole[comp_to_go[0]][comp_to_go[1]].value = self.COMPUTER_O
                break
            else:
                comp_to_go = [random.randint(0,2), random.randint(0,2)]

    def check_winner_horizontal(self, val):
        count = 0
        for row in self.pole:
            for cell in row:
                if cell.value == val:
                    count += 1
                    if count == 3:
                        return True
            count = 0
        return False

    def check_winner_vertical(self, val):
        count = 0
        count_col = 0
        while count_col != 3:
            for i in range(len(self.pole)):
                if self.pole[i][count_col].value == val:
                    count += 1
                    if count == 3:
                        return True
            count = 0
            count_col += 1
        return False

    def check_winner_diagonal(self, val):
        count_1 = 0
        count_2 = 0
        for i in range(len(self.pole)):
            if self.pole[i][i].value == val:
                count_1 += 1
                if count_1 == 3:
                    return True
            elif self.pole[i][len(self.pole)-i-1].value == val:
                count_2 += 1
                if count_2 == 2:
                    return True
        return False

    def check_winner_end(self, val):
        if self.check_winner_diagonal(val) or self.check_winner_horizontal(val) or self.check_winner_vertical(val):
            return True

    def check_draw(self):
        count = 0
        for row in self.pole:
            for cell in row:
                if cell.value == self.FREE_CELL:
                    count += 1
        if count == 0:
            return True
        return False


    @property
    def is_human_win(self):
        return self._is_human_win

    @is_human_win.setter
    def is_human_win(self, val):
        self._is_human_win = val

    @property
    def is_computer_win(self):
        return self._is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, val):
        self._is_computer_win = val

    @property
    def is_draw(self):
        return self._is_draw

    @is_draw.setter
    def is_draw(self, val):
        self._is_draw = val


class Cell:
    def __init__(self):
        self._value = 0

    def __bool__(self):
        return self.value == 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")