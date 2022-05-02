# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 22:20:23 2022


Following along sentdex's "Neural Networks from Scratch" Youtube series.

We set up a basic Neural Network with 2 layers, weights, and ReLU activation.
The weights are randomly initialized and the biases are set to 0.
The input is imported from the dataset "Spiral", with is a set of hundreds of
points (X,y) assembled in the shape of a spiral.
Using matrix multiplication, the input coordinates (X,y) go through 2 layers
of 5 neurons, which output a final two-dimensional result.


@author: Julien Tardy
"""
import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

X, y = spiral_data(100,3)

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)
        
        
layer1 = Layer_Dense(2, 5)
layer2 = Layer_Dense(5, 2)
layer1.forward(X)
activation = Activation_ReLU()
activation.forward(layer1.output)
layer2.forward(activation.output)
activation.forward(layer2.output)
print(activation.output)
