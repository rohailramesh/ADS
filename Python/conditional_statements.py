# if conditions in python do not need a paranthesis unless it is multiple line condition being checked using logical operators

# using if, elif and else
a, b = 1, 2
if a > b:
    print("a is greather than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to be")
    
    

# example of using paranthesis 
x, y, z = 1, 2, 3
if(((x > y) and (y > z)) or ((x < y) and (y < z))):
    print(True)