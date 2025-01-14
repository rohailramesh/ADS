'''
442. Find All Duplicates in an Array
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.

nums[i] must be less than or equal to 105
if nums[i] > 105 -> return [] or if nums[i] < 1 -> return []
'''

# def find_all_duplicates(nums):
#     nums.sort()
#     res_arr = []
#     nums_count_dict = {}
#     for num in nums:
#         if num > 105 or num < 1:
#             return res_arr
#         elif num in nums_count_dict:
#             nums_count_dict[num] = 1 + nums_count_dict.get(num, 0)
#         else:
#             nums_count_dict[num] = 1
#     for num, count in nums_count_dict.items():
#         if count == 2:
#             res_arr.append(num)
#     return res_arr
    
# print(find_all_duplicates([4,3,2,7,8,2,3,1,0]))


# def find_all_duplicates(nums):
#     res = []
#     for i in range(len(nums)-1):
#         print(nums[i])
#         j = i + 1
#         while j != len(nums):
#             if nums[i] == nums[j]:
#                 res.append(nums[i])
#             j += 1
#     return res        

# THE ABOVE 2 ARE MY ATTEMPTS AT THE QUESTION - THEY ARE NOT SATISFYING THE TIME AND SPACE COMPLEXITY REQUIREMENTS BUT DO STILL WORK


# THIS IS AN OPTIMAL SOLUTION EXAMPLE
# Using the same input array to keep track by marking the value as -ve initially and when revisited if it is -ve that means thats a duplicate and add it to the result array and keep doing that for all elements
def find_all_duplicates(nums):
    res = []
    for num in nums:
        num = abs(num)
        if nums[num - 1] < 0:
            print(nums[num], nums[num - 1], num)
            res.append(num)
        nums[num - 1] = -nums[num - 1]
        # print(nums[num], nums[num - 1])
    return res

        
print(find_all_duplicates([4,3,2,7,8,2,3,1]))