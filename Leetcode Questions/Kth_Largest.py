# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import heapq
def findKthLargest(nums, k):
    # negate the list elements
    # heapify the list
    # pop k - 1 elements
    # return the negated element poppped
    for i in range(len(nums)):
        nums[i] = -nums[i]
    heapq.heapify(nums)
    for i in range(k-1):
        heapq.heappop(nums)
    return -heapq.heappop(nums)

k = 2
nums = [3,2,1,5,6,4]
print(findKthLargest(nums, k))