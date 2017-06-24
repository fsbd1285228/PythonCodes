'''Programme for Exercise 6.1 - Lists'''
'''write a small database and some code to query it using lists'''

#import numpy

#Construct the List

FriendList = ['Jack','Lucy','Beta','Sophie','Luella','Audrey','Allen','Will','Jason','Ashe']
FriendYear = [1992,1986,1974,1969,1965,1995,2001,1991,1980,1989]
 
i = 0
j = 0
Check = raw_input('Enter a name: ')
if Check in FriendList:
  i = FriendList.index(Check)
  j = i + 1
  print 'You have 10 friends'
  print '%s is number %d in your list' %(Check, j)
  print '%s was born in %d' %(Check, FriendYear[i])
else:
  print 'This person is not in the list'




#while j <= 9
#  if FriendList[0,j] == Check:
#    print 'You have 10 friends'
#    print '%s is number %d in your list', (%Check, %j+1)
#    print '%s was born in %d', (%Check, %FriendList[1,j])
# else:
  


