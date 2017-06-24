''' A seperate test program for exercise one'''

import exerciseone
if __name__ == '__main__':
    print ('Testing polyOne()')
    x = float(raw_input('Please input x: '))
    y = exerciseone.polyOne(x)
    print 'For x= ', x , 'y= ', y
