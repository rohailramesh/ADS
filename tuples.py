# Similar to arrays but they are immutable so they cannot be modified but can be indexed

myTuple = (0,1,2)
print(myTuple)

# tuples are mainly used as keys for hashmap
myMap = {(1,2) : 3} #mapping key 1 and 2 to value 3
print(myMap)

# tuples can be used as keys for hashsets
mySet = set()
mySet.add((1,2))
print((1,2) in mySet)
# list/arrays cannot be keys