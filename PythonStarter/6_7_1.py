'''Programme for Exercise 6.1 - Lists'''
'''write a small database and some code to query it using lists'''

#import numpy

#Construct the List
FriendList.shape = (10,2)
FriendList[0,0] = 'Jack'
FriendList[0,1] = 'Lucy'
FriendList[0,2] = 'Beta'
FriendList[0,3] = 'Sophie'
FriendList[0,4] = 'Luella'
FriendList[0,5] = 'Audrey'
FriendList[0,6] = 'Allen'
FriendList[0,7] = 'Will'
FriendList[0,8] = 'Jason'
FriendList[0,9] = 'Ashe'
FriendList[1,0] = 1992
FriendList[1,1] = 1986
FriendList[1,2] = 1974
FriendList[1,3] = 1969
FriendList[1,4] = 1965
FriendList[1,5] = 1995
FriendList[1,6] = 2001
FriendList[1,7] = 1991
FriendList[1,8] = 1980
FriendList[1,9] = 1989
 
j = 0
Check = str(raw_input('Enter a name: '))
while j <= 9
  if FriendList[0,j] == Check:
    print 'You have 10 friends'
    print '%s is number %d in your list', (%Check, %j+1)
    print '%s was born in %d', (%Check, %FriendList[1,j])
  else:
  
print 'This person is not in the list'

