# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Plan:
'''
Base case - if array is empty return false
Other cases - 
                Create a loop
                for each iteration, add the current num in dict as key and value as 1
                When adding the next num in array and if it is already in the dict as key then return true as we have found out that there is a duplicate in the dict
'''


def containsDuplicate(nums):
    myDict = {}
    if len(nums) == 0:
        return False
    for num in nums:
        if num in myDict:
            return True
        myDict[num] = 1
    

    


# testing
arr = [1,2,3,4]
print(containsDuplicate(arr))
    
