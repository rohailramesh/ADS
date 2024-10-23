# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3



def majority_element(nums):
    dict = {}
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    print(dict)
    limit = len(nums) / 2
    for num in dict:
        if dict[num] > limit:
            return num
    

nums = [2,2,1,1,1,2,2]
print(majority_element(nums))