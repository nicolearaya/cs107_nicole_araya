'''
The outer function should return a layer object (the inner function). It should take in two arguments:
shape: A list of two numbers where the first number is the number of inputs to the layer and the second number is the number of units in the layer.
actv: An activation function (remember, functions are first class in Python!)
The inner function should return the layer outputs. Remember, the layer outputs are the outputs of each unit in the layer. This function should take in three arguments:
inputs: The inputs to the layer. This should be a numpy array.
weights: The weights for this layer. This should be a matrix of size shape.
bias: The bias for each unit in this layer. This should be a vector of size shape[1] (the number of units in the layer).
'''

#Sharer: Nicole
#Coder: Isha

import numpy as np
from numpy import random

class Layer:
    def __init__(self, shape, actv):
        assert len(shape) == 2 #make sure shape has 2 arguments

        #initialize bias and weights in correct shape with random values from -1 to 1
        bias = np.random.uniform(-1.0, 1.0, size=shape[1])
        weights = np.random.uniform(-1.0, 1.0, size=(shape[0], shape[1]))  

        self.shape = shape
        self.bias = bias
        self.weights = weights
        self.actv = actv 
        
    def forward(self, inputs):
        layer_outputs = np.zeros(self.shape[1])

        for i in range(shape[1]):
            layer_outputs[i] = self.actv(np.dot(self.weights, inputs) + self.bias[i])
        return layer_outputs

    def __str__(self):
        part1 = 'Number of Inputs to Layer: ' + str(self.shape[0]) + ", "
        part2 = 'Number of units in each layer: ' + str(self.shape[1]) + ", "
        part3 = "Activation Function: " + str(self.actv) + ", "
        part4 = "Inputs: " + str(inputs) + ", "
        part5 = "Weights: " + str(weights) + ", "
        part6 = "and Bias: " + str(bias) + "." 
        return(str(part1+part2+part3+part4+part5+part6))
    
    def __repr__ (self):
        return {'numInputsToLayer': self.shape[0], 'numUnitsPerLayer': self.shape[1], 'shape':self.shape, 'actv': self.actv, 'inputs': self.inputs, 'weights': self.weights, 'bias':self.bias}

    def __areBiasesNegative__ (self):
        #returns True if all the biases are negative
        for element in self.bias:
            if (element >=0):
                return False
        return True
    