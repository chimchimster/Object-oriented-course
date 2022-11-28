class LessonItem:
    def __init__(self, title , practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        checking_attrs = {'title': isinstance(value, str),
                          'practices': isinstance(value, int) and value > 0,
                          'duration': isinstance(value, int) and value > 0}

        if checking_attrs[key]:
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if  item in ('title', 'practices', 'duration'):
            raise TypeError
        else:
            object.__delattr__(self, item)

class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = list()

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)

class Course:
    def __init__(self, name):
        self.name = name
        self.modules = list()

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        if len(self.modules) >= 1:
            self.modules.pop(indx)

    def __setattr__(self, key, value):
        if key == 'name' and type(value) == str or type(value) == list:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
print(module_1.__dict__)
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
print(module_2.__dict__)
course.add_module(module_2)
print(module_2.__dict__)
module_2.remove_lesson(1)
print(module_2.__dict__)
