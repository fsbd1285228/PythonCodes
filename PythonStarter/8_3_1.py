''' Example Module. This module contains some example functions and some code for testing them. '''

# Import system modules
import time
def swap(x,y):
    ''' Swaps values of x and y '''
    temp = x
    x = y
    y = temp
    return x, y #Return 2 values

def increment(value, inc=1):
    ''' Increases value by the increment. Default increment is 1 '''
    value = value + inc
    return value # Returns one value

def printMessage(message):
    ''' Print messages to the screenwith a time stamp '''
    now = time.asctime()
    print now, ':', message
    # No return required

def test():
    ''' Perform standard tests on functions in this module '''
    # Test the swap() function.
    value1 = 123; value2 = 987
    printMessage('Testing swap()')
    print 'Initial values:', value1, value2
    value1, value2 = swap(value1, value2)
    print 'Swapped values:', value1, value2
    
    #Test the increment() function.
    start = 123; theIncrement = 2
    printMessage('Testing increment()')
    print 'Start= ', start, 'Increment= ', theIncrement
    new = increment(start, theIncrement)
    print 'Result= ', new

if __name__ == "__main__":
    # This code will run if the module is run directly
    # It will not run if the module is imported
    test() # Run the module standard test function
    # Any other test code can go here