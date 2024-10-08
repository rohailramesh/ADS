# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:

# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

# my attempt
def concatenateArray(nums):
    if len(nums) == 0:
        return 
    # create an array ans of length 2n
    n = len(nums)
    ans = [0] * (2 * n)
    print(ans)
    for i in range(n):
        ans[i] = nums[i]
    for i in range(n):
        ans[i + n] = nums[i]  

    print(ans)
    # time complexity is O(n)
    


# solution
def concatenateArraySol(nums):
    if len(nums) == 0:
        return 
    ans = []
    for i in range(2): #run the outer loop 2 times for 2n requirement
        for num in nums:
            ans.append(num) #append the current num in array at the end of array
    print(ans)
    
    
    
array = [1,2,3,4,5]
concatenateArray(array)