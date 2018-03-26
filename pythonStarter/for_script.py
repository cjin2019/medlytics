
# initialize your variables
str = 'this is a string'
y = 8

# a dictionary is a set of (key,value) pairs, where each key is unique
# here we initialize a dictionary containing 2 items
dict = {'key1':str,
        'key2':y}



print('\nLoop 1 ----------')
# iterate over the characters in str and print them
for letter in str:
    print(letter)


print('\nLoop 2 ----------')
# iterate over a list and add it to y
num_list = [4, 5, 6, 7]
for num in num_list:
    y += num
    print('y = {}'.format(y))


print('\nLoop 3 ----------')
# iterate over a list without pre-defining the list as a separate variable
# note: range(min,max,inc) creates a list from min (inclusive) to max (exclusive) in increments of inc
for z in range(0, 5, 2):
    print(z)


print('\nLoop 4 ----------')
# create an iterator from 0 to the length of str
for j in range(len(str)):
    print(j,':',str[j])             # print the j-th element of 'str'


print('\nLoop 5 ----------')
# loop through all the elements in our dictionary and print out the (key, value) pair
for key,val in dict.items():
    print(key,':',val)


print('\nLoop 6 ----------')
for n in [1, 2, 3, 'foo', 4, 5, 6]:
    print(n)

    # break out of our for-loop if we encounter a variable that is not an integer
    if not isinstance(n,int):
        break


print('\nLoop 7 ----------')
n = 10
for count in range(n):

    #
    count+=1
    #

    print('{}: Print this {} times'.format(count,n))
