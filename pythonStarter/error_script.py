a = 12          # this is an int
b = 'dog'       # this is a string
c = [1, 2, 3]   # this is a list
d = [10]        # this is also a list


# This line will fail because in Python 3 print-statements must be in parentheses
print(b)


# This line will fail because Python can not add an int to a string
x = str(a)+b
print(x)


# This line will fail because Python can not concatenate an int to a list
y = c+[a]
print(y)


# This line will not fail!  Does it do what we think it should do?
z = c+d
print(z)


# This line will fail because if-statements must be followed by a colon
if a > 10:
    print(a)
