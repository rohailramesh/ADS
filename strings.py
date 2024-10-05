# strings are similar to array but they are immutable so they can not be modified
s = 'abcccccc'
print(s[1:3]) #slices string from index 1 to 3 but not including 3

s += 'def' #creates a new string anytime anythign is added. this is O(n) time operation
print(s)

# converting two string to ints and adding them
print(int('123') + int('123')) #converting string '123' to integer and then adding them

# converting an integer to string and adding them just appends the strings together
print(str(123) + str(123))

# printing the ascii value of a character
print(ord("a"))

# to combine a list of strings we can use a delimitor for example a '/'
strings = ['ab','cd','ef']
print("/".join(strings))