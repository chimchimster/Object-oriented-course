class Graph:
    def __init__(self, data, is_show=True):
        self.data = data.copy()
        self.is_show = is_show

    def set_data(self, data):
        self.data = data.copy()

    def show_table(self):
        s = ''
        if self.is_show is False:
            print('Отображение данных закрыто')
        else:
            for i in self.data:
                i = str(i)
                s += str(i) + ' '
            print(s)
        
    def show_graph(self):
        if self.is_show is False:
            print('Отображение данных закрыто')
        else:
            print('Графическое отображение данных:', *self.data)

    def show_bar(self):
        if self.is_show is False:
            print('Отображение данных закрыто')
        else:
            print('Столбчатая диаграмма:', *self.data)
        
    def set_show(self, fl_show):
        self.is_show = fl_show
        
    
data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
