class Graph:
    LIMIT_Y = [0,11]
    
    def set_data(self, data):
        self.data = data

    def draw(self):
        lst = []
        for i in range(len(self.data)):
            if self.data[i] in range(self.LIMIT_Y[0], self.LIMIT_Y[len(self.LIMIT_Y)-1]):
                lst.append(str(self.data[i]))
                x = ' '.join(lst)
        print(x)

    
graph_1 = Graph()
graph_1.set_data([10,-5,100,20,0,80,45,2,5,7])
graph_1.draw()





