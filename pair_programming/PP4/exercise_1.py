import numpy as np

def layer(shape, actv):

    #check that shape is 2
    assert len(shape) == 2

    def h_gen(inputs, weights, bias):
        nonlocal shape
        nonlocal actv

        layer_outputs = np.zeros(shape[1])

        for i in range(shape[1]):
            layer_outputs[i] = actv(np.dot(weights, inputs) + bias[i])

        return layer_outputs

    return h_gen

t = np.random.uniform(0, 1, 100).reshape(-1, 1)
shape1 = np.array([len(t), 4])
shape2 = np.array([len(t), shape1[1]])

layer1 = layer(shape1, np.tanh)
layer2 = layer(shape2, np.tanh)

b1 = np.array([1, 2, 3, 4])
b2 = np.random.uniform(0, 1, shape1[1])

w1 = np.random.normal(0, 1, len(t))
w2 = np.random.normal(0, 2, shape1[1])