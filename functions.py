def functionName(argument1):
    # logic
    pass


# nested functions
def outerFunc(a,b):
    c = 'c'
    def innerFunc():
        return a + b + c
    return innerFunc()

print(outerFunc("a","b"))

# in nested functions, modifying objects is possible but not reassigning them unless declaring the variable as non-local

def double(arr,val):
    def helperFunc():
        for i in enumerate(arr):
            arr[i] *= 2
            
            # val *= 2 #will only modify val in helper scope
            
            # nonlocal val will modify in outer scope too
        nonlocal val
        val *= 2
    helperFunc()
    print(arr, val)
    
nums = [1,2]
val = 3
double(nums,val) #this takes in an array and a value and doubles all the elements in that array and also doubles the value