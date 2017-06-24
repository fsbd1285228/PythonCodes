'''Programme to put some numbers into an array then create a new array of their squares'''

import numpy
x = numpy.array([1.2,6.,15.,21.,3.1]) # creat an array from a list
y = numpy.zeros(len(x), dtype=float) # Creat an array to hold the squares
for i in range(len(x)):
    y[i] = x[i]**2 # Square each element of x and put result in y
print 'Original array: ' , x
print 'Squared array: ' , y