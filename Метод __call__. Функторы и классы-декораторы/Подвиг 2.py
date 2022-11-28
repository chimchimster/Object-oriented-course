class ImageFileAcceptor:
    def __init__(self, extensions):
        self.__extensions = extensions

    def __call__(self, *args, **kwargs):
        for i in args:
            if i.split('.')[-1] in self.__extensions:
                return True

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
acceptor = ImageFileAcceptor(("jpeg", "html"))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]