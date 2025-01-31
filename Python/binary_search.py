# binary search will only work when the list is ascending order
# time complexity of O log(n)
# space complexity of O (1)

def binary_search(nums, target):
    left_pointer = 0
    right_pointer = len(nums) - 1
    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            right_pointer = mid - 1
        elif nums[mid] < target:
            left_pointer = mid + 1
    return False

nums = [4,7,8,11,13,15]
target = 133
print(binary_search(nums, target))