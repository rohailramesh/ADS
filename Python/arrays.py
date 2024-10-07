# these are list in python and are dynamic by default
arr = [1,2,3,4]
print(arr)
arr.append(5) #add 5 to end of arr
print(arr)
arr.pop() #remove last item in arr by default
print(arr)

arr.insert(2,89) #adding 89 at index 2 - Big O(n) operation
print(arr)

arr[0] = 22 #this is a constant time operation
print(arr)

# Initialising an array with a vriable size length
n = 5
var_arr = [1]*n
print(var_arr) #creates an array of length 5 where each element is length 5
print(len(var_arr))

print(arr[-1]) #last value of array

print(arr[1:4]) #slicing the array from index 1 to 4 but not including 4

# unpacking is where you take each of the element from an array and assign them to individual variable. Important that the number of element equal number of variables
# useful when going through list of pairs
a,b,c,d,e = arr
print(a,b,c,d,e)

# looping through array using index
array = [1,2,3,4,5]
for i in range(len(array)):
    print(array[i])
    
# looping through array without index
for element in array:
    print(element)


# looping through an array to print both index and value 
# use enumerate helps you keep track of the index and the value at that index
for i, n in enumerate(array):
    print(i,n)
    
    
# looping through multiple arrays simultaneously using zipping and unpacking
arr_1 = [1,2,3]
arr_2 = [4,5,6]
for a1, a2 in zip(arr_1,arr_2):
    print(a1,a2)


# reversing an array
arr.reverse()
print(arr)

# sorting an array in asc order by default
arr.sort()
print(arr)

# sorting an array in desc order
arr.sort(reverse=True)
print(arr)

# sorting an array which has string values is sorted alphabetically
string_arr = ["alice", "jon", "charlie", "zack"]
string_arr.sort()
print(string_arr)


# sorting an array of strings based on the length of each string
# using a lambda function and pass each value in array as x and find the length of x
string_arr.sort(key= lambda x: len(x))
print(string_arr)