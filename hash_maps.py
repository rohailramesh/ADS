# These are dictionaries in python
# no duplicate keys allows
myMap = {}
myMap["key1"] = "value1"
myMap["key2"] = "value2"
print(myMap)
print(len(myMap)) #returns number of keys in map

myMap["key1"] = "val1"
print(myMap)

print("key1" in myMap) #returns true if key1 in dict

myMap.pop("key1") #deletes the key and the value linekd to it in constant time

# another way of adding key value pairs to hashmaps
myMap2 = {"key1":"value1", "key2":"value2"}
print(myMap2)

# Dict comprehensions 
myMap3 = {i: i*2 for i in range(5)}
print(myMap3)

# looping through maps and printing out the key and the value
for key in myMap3:
    print(key, myMap3[key])

# looping through maps for both key and value but bit more concise
for key, val in myMap3.items():
    print(key, val)
    
# looping through only the values in hashmap 
for value in myMap3.values():
    print(value)
    
    