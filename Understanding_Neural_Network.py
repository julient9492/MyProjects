# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 22:20:23 2022
Following along sentdex's "Neural Networks from Scratch" Youtube series
@author: Julien Tardy
"""
import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

X = [[1, 2, 3 ,2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

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
activation1 = Activation_ReLU()
layer1.forward(X)
activation1.forward(layer1.output)
activation2 = Activation_ReLU()
layer2.forward(activation1.output)
activation2.forward(layer2.output)
print(activation2.output)
