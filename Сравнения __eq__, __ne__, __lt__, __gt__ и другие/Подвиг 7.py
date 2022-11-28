class FileAcceptor:
    def __init__(self, *args):
        self.extensions = [*args]


    def __call__(self, *args, **kwargs):
        for i in self.extensions:
            for j in range(len(args)):
                if i.endswith(args[j][-1]):
                    return True
                else:
                    return False

    def __add__(self, other):
        return FileAcceptor(*(self.extensions + other.extensions))


acceptor = FileAcceptor("jpg", "png", "jpeg") #выделяем только файлы с расширениями картинок
filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
filenames = list(filter(acceptor, filenames))
print(filenames)