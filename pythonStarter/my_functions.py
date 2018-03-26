

def make_plural(in_string):
    """ This function adds an 's' to the end of an input string. """
    out_string = in_string + 's'
    return out_string



def raise_to_power(base,power=1):
    """ This function raises a base value to a power value """
    return base**power



# initialize variables
thing = 'dog'
x = 10
y = 3


# call the make_plural function to add an 's' to our string
thing2 = make_plural(thing)
print('thing:',thing)
print('thing2:',thing2)


# call our raise_to_power function using the input variable order as in the function definition
a = raise_to_power(x,y)
print('a:',a)


# call our raise_to_power function  without specifying the power
b = raise_to_power(x)
print('b:',b)


# call our raise_to_power function  while specifying the input variables (notice the order is changed!)
c = raise_to_power(power=y,base=x)
print('c:',c)
