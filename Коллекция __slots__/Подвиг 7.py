class Note:
    _avaliable_names = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си',
    _avaliable_tons = -1, 0, 1,

    def __init__(self, name, ton=0):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in self._avaliable_names:
            raise ValueError('недопустимое значение аргумента')

        if key == '_ton' and value not in self._avaliable_tons:
            raise ValueError('недопустимое значение аргумента')

        object.__setattr__(self, key, value)

class Notes:
    _instance = None
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si',
    _avaliable_names = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си',


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __del__(self):
        Notes._instance = None


    def __init__(self):
        for k, v in zip(self.__slots__, self._avaliable_names):
            setattr(self, k, Note(v, 0))


    def __getitem__(self, item):
        if not (0 <= item < 7):
            raise IndexError('недопустимый индекс')

        return getattr(self, self.__slots__[item])



notes = Notes()
nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = 1 # изменение тональности ноты фа
print(notes[3]._ton)
notes[3]._ton = -1