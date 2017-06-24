'''Exercise one'''

def polyOne(x):
    y = x*x*x - 7*x*x + 14*x -5
    return y

x = float(raw_input('Please input x: '))
y = polyOne(x)
print 'For x= ', x, 'y= ', y