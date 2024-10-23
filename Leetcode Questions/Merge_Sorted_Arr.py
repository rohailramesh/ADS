'''
Given two arrays nums1 and nums2. nums1 has length m and nums2 has n
Have to return nums1 with elements merged from both arrays and sorted in desc order. 

EG: nums1 = [1,2,3,0,0,0] nums2 = [4,5,6]
should return [1,2,3,4,5,6]

Pattern to use here would be the two pointer pattern
Since we have to replace the 0's with actual elements, it is better to start at the end of the array and move backwards to the start fro nums1 and nums2.

Oncce we move back and reach to the start of array we should have all the elements merged and sorted in nums1.

Other case to consider is that once we move back to start of nums1 but there are elements left in nums2 then we can just fill nums1 with them
'''

def merge(nums1, nums2, m, n):
    # find last index in nums1 initially when there is 0's too in list
    last_index_in_nums1 = m + n - 1
    
    # start moving the pointer back to start and merge as you do that
    while m > 0 and n > 0: # this is to check we are still in bound in both lists
        if nums1[m-1] > nums2[n-1]: # checks if current value in nums1 is greater than current value in nums2 and if it is, then replace value in last index position with that value since we want in desc order
            nums1[last_index_in_nums1] = nums1[m-1]
            m -= 1 #moving towards start of nums1
        else:
            nums1[last_index_in_nums1] = nums2[n-1]
            n -= 1
        last_index_in_nums1 -= 1
    while n > 0: #once you get back to start of nums1 and nums2 still has elements, you can just add them at start of nums1 since they are in desc order already
        nums1[last_index_in_nums1] = nums2[n-1]
        n, last_index_in_nums1 = n-1, last_index_in_nums1-1
    return nums1

nums1 = [3,2,6,0,0,0,0]
nums2 = [1,7,5]
m = 3
n = 3
print(merge(nums1,nums2,m,n))

