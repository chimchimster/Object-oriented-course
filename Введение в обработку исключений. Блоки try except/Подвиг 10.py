class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value, *args, **kwargs):
        if not (self.min_value <= value <= self.max_value) or not isinstance(value, float) or isinstance(value, bool):
            raise ValueError('значение не прошло валидацию')
        return value


class IntegerValidator(FloatValidator):
    def __call__(self, value, *args, **kwargs):
        if not (self.min_value <= value <= self.max_value) or not isinstance(value, int) or isinstance(value, bool):
            raise ValueError('значение не прошло валидацию')
        return value


def is_valid(lst, validators):
    l = []
    for element in lst:
        for validator in validators:
            try:
                l.append(validator(element))
            except:
                continue
    return l

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print(lst_out)
