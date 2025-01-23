'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

def three_sum(nums):
    res = []
    n = len(nums)
    
    # Iterate over all possible triplets
    for p1 in range(n - 2):  # First pointer
        print(p1)
        for p2 in range(p1 + 1, n - 1):  # Second pointer
            print(p2)
            for p3 in range(p2 + 1, n):  # Third pointer
                print(p3)
                if nums[p1] + nums[p2] + nums[p3] == 0:
                    triplet = sorted([nums[p1], nums[p2], nums[p3]])
                    if triplet not in res:  # Avoid duplicates
                        res.append(triplet)
    return res

# Test the function
print(three_sum([-1, 0, 1, 2, -1, -4]))


def three_sum_optimised(nums):
    nums.sort() #this has a time complexity of O(n log n)
    res = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:#if the two adjacent vals are the same then move on as we don't want duplicates
            continue
        left_pointer, right_pointer = i + 1, len(nums) - 1
        while left_pointer < right_pointer: #since we already have a value for the first triplet, we can use the two sum technique using two pointers to find the second and third while following the rules
            three_sum = a + nums[left_pointer] + nums[right_pointer]
            if three_sum > 0:
                right_pointer -= 1
            elif three_sum < 0:
                left_pointer += 1
            else:
                res.append([a, nums[left_pointer], nums[right_pointer]])
                left_pointer += 1
                while nums[left_pointer] == nums[left_pointer-1] and left_pointer < right_pointer:
                    left_pointer += 1
    return res
    
print(three_sum_optimised([-1, 0, 1, 2, -1, -4]))