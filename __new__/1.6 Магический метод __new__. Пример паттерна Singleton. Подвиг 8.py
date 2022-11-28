TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    name = None
    obj = None
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            cls.obj = super().__new__(DialogWindows)
            cls.obj.name = args[0]
            return cls.obj
        else:
            cls.obj = super().__new__(DialogLinux)
            cls.obj.name = args[0]
            return cls.obj

    def __init__(self, name):
        self.name = name

dlg = Dialog('a')
print(dlg)