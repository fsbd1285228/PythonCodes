'''This program aims to generate the first 10 elements of a Fibonacci series of integers'''
import numpy
x = numpy.zeros(10, dtype=int)
a = 0
b = 1
c = a + b
ratio = c/b
i = 0
while ratio>10e-10:
    ratio = c/b
    i = i+1
    #temp = a
    a = b
    b = c
    c = a+b    
print 'Value of Golden ratio is %f after %d iterations' %(ratio,i)