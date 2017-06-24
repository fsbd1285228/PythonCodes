a = float(raw_input('Please enter a positive number: '))
if a < 0:
  print 'That is a negative number'
  print 'That is not what I asked for'
elif a > 0:
  print 'Thank you'
  print 'That is a positive number'
else:
  print 'That looks like zero to me'