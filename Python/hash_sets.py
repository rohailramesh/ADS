# Insert values in constant time and also search in constant time since every value in the set is unique and a hash created for each value must also be unique then
mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(2) # won't add another 2 since a hash set only accpets unique values
print(mySet)
print(len(mySet))

# check if a certain value is in a hash set
print(1 in mySet) #returns boolean value

# changing a list/array into a set
print(set([1,2,3]))

# set comprehension
mySet2 = {i for i in range(5)}
print(mySet2)