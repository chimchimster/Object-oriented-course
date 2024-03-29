class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = list()

    def add_app(self, app):
        flag = True
        for i in self.apps:
            if type(i) == type(app):
                flag = False
        if flag:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)

class AppVK:
    def __init__(self, name='ВКонтакте'):
        self.name = name

class AppYouTube:
    def __init__(self, memory_max=1024, name='YouTube'):
        self.memory_max = memory_max
        self.name = name

    def __setattr__(self, key, value):
        if key == 'memory_max' and type(value) == int and value > 0 or type(value) == str:
            object.__setattr__(self, key, value)
        else:
            raise TypeError('Параметр должен быть целым положительным числом!')

class AppPhone:
    def __init__(self, phone_list, name='Phone'):
        self.name = name
        self.phone_list = phone_list

    def __setattr__(self, key, value):
        if key == 'phone_list' and type(value) == dict or type(value) == str:
            object.__setattr__(self, key, value)
        else:
            raise TypeError('Параметр должен быть словарем!')



app_1 = AppVK()
app_2 = AppYouTube(1024)
app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112})
print(app_1.__dict__)
print(app_2.__dict__)
print(app_3.__dict__)

sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)