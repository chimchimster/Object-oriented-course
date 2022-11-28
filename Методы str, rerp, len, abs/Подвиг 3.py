import re
class Model:
    def __init__(self):
        self.model = ''

    def query(self, **kwargs):
        self.model += str(kwargs)

    def __str__(self):
        if len(self.model) == 0:
            return 'Model'
        x = f'Model: {self.model.replace("{","").replace("}", "").replace(":", " =")}'
        return x.replace('\'', '')

m = Model()
m.query(id=1, fio='Sergey', old=33)
print(m)

