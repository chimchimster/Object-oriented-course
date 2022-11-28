from random import randint, sample, choice

class GamePole:
    _instance = 0

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


    def __init__(self,N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = tuple([tuple(Cell() for x in range(self.M)) for _ in range(self.N)])

    @property
    def pole(self):
        return self.__pole_cells

    @pole.setter
    def pole(self, value):
        self.__pole_cells = value

    def set_attr_is_mine_pole(self, new_pole):
        new_pole = list(map(lambda x: list(x), new_pole))
        for i in range(self.total_mines):
            new_pole[randint(0, len(new_pole)-1)][randint(0, self.M-1)].is_mine = True
        for i in new_pole:
            for _j in i:
                if hasattr(_j, 'is_open'):
                    setattr(_j, 'is_open', False)
        return new_pole

    def init_pole(self):
        self.pole = self.set_attr_is_mine_pole(self.pole)
        self.count_mines(self.pole)
        return self.pole



    def open_cell(self, i, j):
        if i not in range(self.N) or j not in range(self.M):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True



    def show_pole(self):
        counter = 0
        for i in self.pole:
            for j in i:
                if j.is_open:
                    if j.is_open and j.is_mine:
                        print('B', end = ' ')
                print('*', end=' ')
                counter += 1
            else:
                    print('O', end = ' ')
                    counter += 1
                    if counter == self.M:
                        print(end = '\n')
                        counter = 0


    def count_mines(self, pole):
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.N):
            for y in range(self.M):
                if not pole[x][y].is_mine:
                    mines = sum((pole[x + i][y + j].is_mine for i, j in indx if
                                 0 <= x + i < self.N and 0 <= y + j < self.M))
                    pole[x][y].number = mines


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False




    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if type(value) == bool:
            self.__is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if value in range(0,9):
            self.__number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) == bool:
            self.__is_open = value
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        if self.is_open:
            return False
        elif not self.is_open:
            return True


if __name__ == '__main__':
    g = GamePole(5, 5, 10)
    g.init_pole()
    g.open_cell(1,1)
    g.open_cell(2,1)
    g.open_cell(3,1)
    g.open_cell(3,1)
    g.open_cell(0,1)
    g.show_pole()