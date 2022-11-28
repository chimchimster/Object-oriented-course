CURRENT_OS = 'windows'   # 'windows', 'linux'

class FileDialogFactory:
    def __new__(cls, title, path, exts, *args, **kwargs):
        if title and path and exts:
            return cls.create_windows_filedialog(title, path, exts) if CURRENT_OS == 'windows' else cls.create_linux_filedialog(title, path, exts)


    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)



class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts

dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
print(dlg.__dict__)