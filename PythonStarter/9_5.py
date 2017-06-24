'''Program to demonstrate try/expect in action'''

import numpy

def analyse(data,num):
    # Analyse 'num' samples from the data
    sample = 0 # The index of the sample in the data array
    samplesUsed = 0 # Number of samples used
    try:
        while samplesUsed < num:
            if data[sample] > 0.2: # Apply a threshold
                result = data[sample] * 1.23 + 2.34 # The algorithm
                samplesUsed += 1
                sample += 1 # Next sample
    except IndexError: # Catch the indexing error
                pass # Do nothing. block cannot be empty
    return result, samplesUsed # Return result and samples used

def getTheData():
    # Get all the data to be analysed from file.
    # This is a dummy version that gets some random numvers
    return numpy.random.rand(113) # Generate 113 random numvers (0 to 1)

if __name__ == "__main__":
    # Test code
    theData = getTheData() # Get the data set to be analysed
    sampleSize = 100
    answer, samples = analyse(theData, sampleSize)
    print 'Used ', samples, ' samples. The result is : ', answer