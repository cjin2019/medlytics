

# This is a comment.
# Anything typed here will be ignored by the code.
# But comments are useful for humans who are trying to read the code!


# This is how we import a python library!
import math

# If you try to run this code and get an error saying the library can't be found, go to a terminal and type:
#       conda install datetime
import datetime


# Let's define some variables!
a = 10
b = 3
jane = 'Jane Doe'
john = 'John Doe'


# Let's print out the variables!
print('a: ',a)
print('b: ',b)
print('jane: ',jane)
print('john: ',john)


# Adding variables
c = a + b
d = a - b
print('c: ',c)
print('d: ',d)


# See what happens when we try to "add" strings
family = jane + john
print('family: ',family)


# Let's use python's math library to calculate a^b
e = math.pow(a,b)
print('e: ',e)


# Let's see what time it is
now = datetime.datetime.now()
print('It is now: ',now)
