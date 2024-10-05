'''
Problem -> Given an array of integers and an integer target, return indices of two numbers in array such that they add to
give target

Plan -> 1. Create a dictionary to store numbers from array as keys and indices as values
        2. Iterate through array adding each number to dict
        3. Inside the loop, check if target - current num equals to 
'''



'''
How dictionary stores key values pairs:


'''

def twoSum(nums, target):
    nums_dict = {} # create a dictionary to store nums as keys and their indices as values
    for i in range(len(nums)): # loop through the entire array
        if target - nums[i] in nums_dict: # if the difference between target and current value of index is in the dict at that point
            return [nums_dict[target - nums[i]],i] # then return the indices for that current index and 
        nums_dict[nums[i]] = i

nums = [2,7,11,15] 
target = 9

# print(twoSum(nums, target))

def testFunc(nums):
    for i in range(len(nums)):
        print(nums[i])

testFunc([1,2,3,4,5,6,7])