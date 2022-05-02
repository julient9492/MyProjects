# -*- coding: utf-8 -*-
"""
Created on Mon May  2 12:57:33 2022

Introduction to Softmax activation function
which is use on layer2
@author: Julien Tardy
"""
import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

X, y = spiral_data(samples=100, classes = 3)

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)
        
        
class Activation_Softmax:
    def forward (self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities
    
layer1 = Layer_Dense(2, 3)
layer2 = Layer_Dense(3, 3)
layer1.forward(X)
activation = Activation_ReLU()
activation.forward(layer1.output)
layer2.forward(activation.output)
activation2 = Activation_Softmax()
activation2.forward(layer2.output)
print(activation2.output)

