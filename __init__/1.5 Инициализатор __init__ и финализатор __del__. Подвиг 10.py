import random

class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.n = N
        self.m = M
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]
        self.init()

    def init(self):
        while self.m != 0:
            r, c = random.randint(0, self.n-1), random.randint(0, self.n-1)
            if self.pole[r][c].mine == False:
                self.pole[r][c].mine = True
            else:
                continue
            self.m -= 1


        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.n):
            for y in range(self.n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x+i][y+j].mine for i, j in indx if 0 <= x + i < self.n and 0 <= y + j < self.n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        for x in self.pole:
            for y in x:
                if not y.fl_open:
                    print('#', end=' ')
                else:
                    print('*', end=' ')
            print()

pole_game = GamePole(10, 12)
pole_game.show()
