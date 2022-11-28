class DescrStr:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__check_type(value)
        setattr(instance, self.name, value)

    @classmethod
    def __check_type(cls, val):
        if not isinstance(val, str):
            raise TypeError('неверный тип аргумента')


class DescrNumber:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__check_type(value)
        setattr(instance, self.name, value)

    @classmethod
    def __check_type(cls, val):
        if not (isinstance(val, (int, float)) and val > 0):
            raise TypeError('неверный тип аргумента')


class Aircraft:
    _model = DescrStr()
    _mass = DescrNumber()
    _speed = DescrNumber()
    _top = DescrNumber()

    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        if isinstance(chairs, int) and chairs > 0:
            self._chairs = chairs
        else:
            raise TypeError('неверный тип аргумента')

class WarPlane(Aircraft):
    def __init__ (self, model, mass, speed, top, weapons=None):
        super().__init__(model, mass, speed, top)
        if isinstance(weapons, dict):
            self._weapons = weapons
        else:
            raise TypeError('неверный тип аргумента')

planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
