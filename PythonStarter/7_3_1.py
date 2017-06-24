'''Exercise 1'''
import numpy
x = numpy.arange(6.0)
y = numpy.zeros(len(x), dtype=float)
z = numpy.zeros(len(x), dtype=float)
for i in range(len(x)):
    y[i] = x[i]**2
    z[i] = x[i]**3
print 'The first array is :\n', x
print 'The second array is :\n', y
print 'The third array is :\n', z
