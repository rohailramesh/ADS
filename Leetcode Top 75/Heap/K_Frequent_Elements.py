'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''
# This approach is without the use of heaps and is not optimised
def k_frequent_elements(nums, k):
    res = []
    if not nums or k < 1 or k > len(set(nums)):
        return []
    nums_count = {}
    for num in nums:
        if num in nums_count:
            nums_count[num] += 1
        else:
            nums_count[num] = 1
    
    sorted_elements = sorted(nums_count.items(), key=lambda x: x[1], reverse=True)
    print(sorted_elements)
    for element, _ in sorted_elements[:k]:
        res.append(element)
    return res


print(k_frequent_elements([1,1,1,2,2,3], 2))



'''
sorted_elements = sorted(nums_count.items(), key=lambda x: x[1], reverse=True)

How the above works:
- .items() returns all key-value pair as tuples in a list
- sort that tuple based on a lambda function
- the key used here is that we will sort the tuples based on the frequency value which is at position [i]
- set reverse = True for descending order
'''


# This approach is with the use of heaps and is optimised
import heapq
from collections import Counter
def topKFrequent(nums, k):
    # similar approach to above but in this one, use min heap approach
    # to speed things up with setting up a dictionary to keep track of frequency, we can use collections from Counter which does the same thing
    counter = Counter(nums)
    heap = []
    for key, val in counter.items():
        if len(heap) < k: #the heap should have k elements but if it is less than k then we can just heap push the key and val but in this format: (val, key) since it is a min heap, it will be in ascending order
            heapq.heappush(heap, (val, key))
        else: #if we have more than k, we can pop the smallest pair which will be the first one and push the next pair simultaneously 
            heapq.heappushpop(heap, (val, key))
    print(heap)
    return [h[1] for h in heap]
print(topKFrequent([1,1,1,2,2,3], 2))
# This has a time complexity of O(n * log(k)) and space complexity of O(n)