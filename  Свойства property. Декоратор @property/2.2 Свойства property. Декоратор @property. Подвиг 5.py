class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = self.__height = None
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) == int and 0 <= w <= 10000:
            if self.__width:
                self.show()
            self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if type(h) == int and 0 <= h <= 10000:
            if self.__height:
                self.show()
            self.__height = h

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

