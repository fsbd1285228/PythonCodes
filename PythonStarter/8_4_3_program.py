'''Functions to pick out the maximum and minimum value in a list'''

def maximum(a):
    ''' Pick out the maximum value in the given list. '''
    maximum = a[0]
    for i in range(a):
        if maximum < a[i]:
            maximum = a[i]
        else:
            i +=1
    return maximum


def minimum(a):
    ''' Pick out the minimum value in the given list. '''
    minimum = a[0]
    for i in range(a):
        if minimum > a[i]:
            minimum = a[i]
        else:
            i +=1
    return minimum

