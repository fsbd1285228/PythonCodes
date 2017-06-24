'''Program to restrict the values of an array to less than 2*pi'''

import numpy 
x= numpy.arange(0.,10.,0.2) # Create an array using numpy.arange
print 'The original array:\n', x
for i in range(len(x)): # Loop over a range from 0 up to the length of x
    if (x[i] > 2*numpy.pi):
        x[i] = x[i] - 2*numpy.pi # Restrict the data to < 2* pi
print 'The restricted array:\n', x # would this work for all input values?