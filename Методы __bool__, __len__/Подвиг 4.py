class CheckStr:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_type(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_type(cls, value):
        if type(value) == str:
            return True
        else:
            raise ValueError('not STR!')

class CheckInt:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_type(value):
            setattr(instance, self.name, value)

    @classmethod
    def __check_type(cls, value):
        if type(value) == int:
            return True
        else:
            raise ValueError('not INT!')

class Player:
    name = CheckStr()
    old = CheckInt()
    score = CheckInt()

    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score


    def _check_score(self):
        if self.score > 0:
            return True
        else:
            return False

    def __bool__(self):
        return self._check_score()


lst_in = ['Балакирев; 34; 2048',
'Mediel; 27; 0',
'Влад; 18; 9012',
'Nina P; 33; 0']

lst_in = [x.split(';') for x in lst_in]
for i in lst_in:
    i[1], i[2] = int(i[1]), int(i[2])
players = [Player(*x) for x in lst_in]
print(players)
players_filtered = sorted(players, key=bool)
players_filtered = list(filter(bool, players_filtered))
for i in players_filtered:
    print(i.score)
