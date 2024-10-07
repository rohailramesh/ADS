import math
# division is decimal by default
print(5/2) #will print 2.5 and not 2 like other prgrams where it rounds round

print(5//2) #will do division and return an integer rounded down

# negaive division will round down instead towards 0
print(-3//2)

# to overcome the problem of rounding down in negative division: convert the normal negtive division to an int
print(int(-3/2))

# modulo operator gives the remainder
print(4 % 2)
print(math.fmod(-10, 3))

# rounding down
print(math.floor(5.5))

# rounding up
print(math.ceil(5.5))

# square root
print(math.sqrt(169))

# power
print(math.pow(5,4))

# to use max or min infinity
float("inf")
float("-inf")