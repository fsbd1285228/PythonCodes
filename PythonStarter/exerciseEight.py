'''Exercise one'''

def polyOne(x):
    y = x*x*x - 7*x*x + 14*x -5
    return y

def maximum(a):
    ''' Pick out the maximum value in the given list. '''
    maximum = a[0]
    for i in range(a):
        if maximum < a[i]:
            maximum = a[i]
        i +=1
    return maximum


def minimum(a):
    ''' Pick out the minimum value in the given list. '''
    minimum = a[0]
    for i in range(a):
        if minimum > a[i]:
            minimum = a[i]
        i +=1
    return minimum


