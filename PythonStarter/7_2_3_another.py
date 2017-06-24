''' An example of using the numpy.where function. Have the same function with 7_3 in a more simple way'''

import numpy

x = numpy.arange(0.,10.,0.2)
print 'The origginal array:\n', x
x = numpy.where(x>2*numpy.pi, x-2*numpy.pi, x) 
print 'The restricted array:\n', x