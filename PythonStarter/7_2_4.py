'''Program to sort some numbers into ascending order'''
import numpy
# Create some floating numbers as a list and convert to an array
x = numpy.array([23.2,12.1,1.2,34.6,0.1,15.2,19.3,45.6,3.4])
print ' The original array:\n', x
for cycle in range(len(x)):    # Cycle enough times so that sort is complete
    for i in range (len(x)-1):    # Correct order of each pair of values
        if x[i] > x[i+1]:
            temp = x[i]
            x[i] = x[i+1]
            x[i+1] = temp
    print 'The array after cycle ', cycle, ':\n',x
print 'The ordered array:\n',x
        
    