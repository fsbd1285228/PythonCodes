# -*- coding: utf-8 -*-
''' 

This sample code for neural network studies a simple network with the following structure:

a1 --
      --(w1)
            --
                -- b  (+bias) -- h
            --    
      --(w2)
a2 --

'''

import numpy as np


class FullyConnect:
    def __init__(self, l_x, l_y):  # Here the two parameters represents the length of the input layer and output layer
        self.weights = np.random.randn(l_y, l_x)  # Initialize the parameter (weights) with random numbers
        self.bias = np.random.randn(1)  # Initialize the parameter (bias) with random numbers

    def forward(self, x):
        self.x = x  # Save the intermediate result in prepare of the counter propagation
        self.y = np.dot(self.weights, x) + self.bias  # Calculate: w11*a1+w12*a2+bias1
        return self.y  # Delivery the result of this layer forward

    def backward(self, d):
        self.dw = d * self.x  # According to the chain rule, multiply the returned derivative value with x to obtain the gradient of the parameter
        self.db = d
        self.dx = d * self.weights
        return self.dw, self.db  # Return the calculated parameter gradient. Note that if it continues the gradient of counter propagation here, self.dx should be returned


class Sigmoid:
    def __init__(self):  # No parameters so no need to initialize
        pass

    def sigmoid(self, x):
        return 1 / (1 + np.exp(x))

    def forward(self, x):
        self.x = x
        self.y = self.sigmoid(x)
        return self.y

    def backward(self):  # Since in this example the Sigmoid function is the last layer, we start calculating the gradient of counter propagation here
        sig = self.sigmoid(self.x)
        self.dx = sig * (1 - sig)
        return self.dx  # The gradient of Counter-propagation


def main():
    fc = FullyConnect(2, 1)
    sigmoid = Sigmoid()
    x = np.array([[1], [2]])
    print 'parameters: weights:', fc.weights, ' bias:', fc.bias, ' input: ', x

    # The Forward Algorithm
    y1 = fc.forward(x)
    y2 = sigmoid.forward(y1)
    print 'forward result: ', y2

    # Counter-propagation
    d1 = sigmoid.backward()
    dx = fc.backward(d1)
    print 'backward result: ', dx


if __name__ == '__main__':
    main()
