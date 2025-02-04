def contains_duplicate(nums):
    nums_set = set()
    if not nums:
        return True
    for num in nums:
        if num in nums_set: #this means there is a duplicate so return True
            return True
        nums_set.add(num) #else add the current number to the set
    return False

print(contains_duplicate([1,2,3,4,5,6,7,8,9]))

# Time complexity of O(n)
# Space complexity of O(n)


# Time complxities of different operations in Sets data structures:
'''
set.remove() -> O(1)
set.discard() -> O(1) Discard does not raise an error but remove does if the element to be deleted is not found

to get an item from the set or to check if item is in set -> O(1)
Getting the size of the set O(1)

copy() has a time complexity of O(n)
'''