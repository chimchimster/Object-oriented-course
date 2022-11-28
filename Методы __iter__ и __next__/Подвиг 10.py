class Matrix:
    def __init__(self, rows_or_list, cols=0, fill_value=0):
        if type(rows_or_list) == list:
            self.rows = len(rows_or_list)
            self.cols = len(rows_or_list[0])
            if not all(len(r) == self.cols for r in rows_or_list) or \
                not all(self._is_digit(x) for row in rows_or_list for x in row):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.lst = rows_or_list
        else:
            if type(rows_or_list) != int or type(cols) != int or type(fill_value) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

            self.rows = rows_or_list
            self.cols = cols
            self.lst = [[fill_value for _ in range(cols)] for _ in range(rows_or_list)]


    @staticmethod
    def _is_digit(x):
        return type(x) in (int, float)

    def __check_index(self, val):
        r, c = val
        if not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError('недопустимые значения индексов')


    def __getitem__(self, item):
        self.__check_index(item)
        row, col = item
        return self.lst[row][col]

    def __setitem__(self, key, value):
        self.__check_index(key)
        if not self._is_digit(value):
            raise TypeError('значения матрицы должны быть числами')
        row, col = key

        self.lst[row][col] = value

    def __check_dimensions(self, other):
        rows, cols = other.rows, other.cols
        if self.rows != rows or self.cols != cols:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        if type(other) == type(self):
            self.__check_dimensions(other)
            return Matrix([[self[i,j] + other[i,j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self._is_digit(other)
            return Matrix([[self[i,j] + other for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if type(other) == type(self):
            self.__check_dimensions(other)
            return Matrix([[self[i, j] - other[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self._is_digit(other)
            return Matrix([[self[i, j] - other for j in range(self.cols)] for i in range(self.rows)])


list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"