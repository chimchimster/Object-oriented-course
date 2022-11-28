class Vector:
    _allowed_types = (int, float)

    def __init__(self, *coords):
        self._check_coords(coords)
        self._coords = coords

    def _check_coords(self, coords):
        if not all(type(x) in self._allowed_types for x in coords):
            raise ValueError('неверный тип координат')

    def get_coords(self):
        return tuple(self._coords)

    @staticmethod
    def _is_vector(obj):
        if not isinstance(obj, Vector):
            raise TypeError('Операнд должен быть объектом класса Vector или другого дочернего класса')

    def _check_vector_dims(self, other):
        if len(self._coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')

    def _make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self._is_vector(other)
        self._check_vector_dims(other)

        coords = tuple(a + b for a, b in zip(self._coords, other.get_coords()))
        return self._make_vector(coords)

    def __sub__(self, other):
        self._is_vector(other)
        self._check_vector_dims(other)

        coords = tuple(a - b for a, b in zip(self._coords, other.get_coords()))
        return self._make_vector(coords)

class VectorInt(Vector):
    _allowed_types = (int, )
