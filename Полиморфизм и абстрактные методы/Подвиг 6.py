from abc import ABC, abstractmethod

class Model:
    @abstractmethod
    def get_pk(self):
        raise TypeError

    @classmethod
    def get_info(cls):
        return f'Базовый класс {cls.__name__}'

class ModelForm(Model):
    instance_id = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.generate_id()

    @classmethod
    def generate_id(cls):
        cls.instance_id += 1
        return cls.instance_id

    def get_pk(self):
        return self._id

form = ModelForm("Логин", "Пароль")
print(form.get_pk())