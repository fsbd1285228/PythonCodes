'''This program aims to generate the first 10 elements of a Fibonacci series of integers'''
import numpy
x = numpy.zeros(10, dtype=int)
x[0] = 0
x[1] = 1
for i in range(len(x)-2):
    x[i+2] = x[i] + x[i+1]
print 'The first 10 elements of a Fibonacci series of integers is :\n', x
