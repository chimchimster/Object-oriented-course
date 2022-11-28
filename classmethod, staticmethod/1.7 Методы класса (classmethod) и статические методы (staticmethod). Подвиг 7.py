from string import ascii_lowercase, digits

class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    start = 3
    stop = 50

    def __init__(self, name):
        self.name = name
        self.size = 10
        if not self.check_name(self.name):
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        flag = True
        for letter in name:
            if letter in [i for i in cls.CHARS_CORRECT]:
                continue
            else:
                flag = False
        return cls.start <= len(name) <= cls.stop and flag

class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    start = 3
    stop = 50

    def __init__(self, name):
        self.name = name
        self.size = 10
        if not self.check_name(self.name):
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


    @classmethod
    def check_name(cls, name):
        flag = True
        for letter in name:
            if letter in [i for i in cls.CHARS_CORRECT]:
                continue
            else:
                flag = False
        return cls.start <= len(name) <= cls.stop and flag


# здесь объявляйте классы TextInput и PasswordInput


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
print(html)