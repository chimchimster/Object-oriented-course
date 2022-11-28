class Layer:
    def __init__(self, name='Layer'):
        self.next_layer = None
        self.name = name

    def __call__(self, layer, *args, **kwargs):
        self.next_layer = layer
        return layer

class Input(Layer):
    def __init__(self, inputs):
        super().__init__('Input')
        self.inputs = inputs if type(inputs) is int else None


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__('Dense')
        self.inputs = inputs if type(inputs) is int else None
        self.outputs = outputs if type(outputs) is int else None
        self.activation = activation if type(activation) is str else None

class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        while self.network:
            yield self.network
            self.network = self.network.next_layer

network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

for x in NetworkIterator(network):
    print(x.name)