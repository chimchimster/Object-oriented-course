class Validator:
    def _is_valid(self, data):
        return True

    def __call__(self, data, *args, **kwargs):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')

class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.diapasone = range(min_value, max_value + 1)

    def _is_valid (self, data):
        return data in self.diapasone and type(data) is int

class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.diapasone = range(min_value, max_value + 1)

    def _is_valid(self, data):
        return data in self.diapasone and type(data) is float

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
#res2 = float_validator(10)    # исключение ValueError
