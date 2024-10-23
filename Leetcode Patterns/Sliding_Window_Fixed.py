# Given an array, to find a sub array of some thing for example the max sum of a fixed length sub contiguous array, use sliding window pattern

'''
Example: Given an integer array of n elements and integer k, find contiguous array in the array whose length is equal to k that has maximum average value
'''

def findMaxAverage(nums, k):
    n = len(nums)
    current_sum = 0
    max_avg = current_sum / k
    for i in range(k):
        current_sum += nums[i]
    for i in range(k,n):
        current_sum += nums[i]
        current_sum -= nums[i-k]
        avg = current_sum/k
        max_avg = max(avg, max_avg)
    return max_avg

nums = [1,12,-5,-6,50,3]
k=4
print(findMaxAverage(nums,k))