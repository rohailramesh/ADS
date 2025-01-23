'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

def two_sum_solution1(arr, target):
    # This solution only works if the array is sorted becuase when returning the indices of two values found, it uses the old array and if it wasn't sorted then it would not return the right indices.
    # Sort the array
    arr.sort()

    left, right = 0, len(arr) - 1

    # Iterate while left pointer is less than right
    while left < right:
        sum = arr[left] + arr[right]

        # Check if the sum matches the target
        if sum == target:
            return [left+1,right+1]
        elif sum < target: 
            left += 1  # Move left pointer to the right
        else:
            right -= 1 # Move right pointer to the left

    # If no pair is found
    return False
            
nums_2 = [2,5,7,11]
print(two_sum_solution1(nums_2, 9))


def two_sum_solution2(nums, target):
    # This solution uses dict to check if the target - current value in loop is in dict and if it is then it returns the current val and ith key from dict
    numToIndex = {}
    for i in range(len(nums)):
        if target - nums[i] in numToIndex:
            return [numToIndex[target - nums[i]], i]
        numToIndex[nums[i]] = i
    return []
nums_2 = [2,7,5,11]
print(two_sum_solution2(nums_2, 9))