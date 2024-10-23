# Using two pointers simultaneously to find the target value. For example given a sorted array, we can use two pointers - one at index 0 and one at index[-1] and reach the middle while finding a target value achieved when we add two specific numbers in the array

def two_sum(array, target):
    left_pointer, right_pointer = 0, len(array) - 1
    # print(left_pointer, right_pointer)
    # for i in range(len(array)):
    #     print(array[i])
    while left_pointer < right_pointer:
        current_target = array[left_pointer] + array[right_pointer]
        if target == current_target:
            return array[left_pointer], array[right_pointer]
        if current_target > target:
            right_pointer -= 1
        else:
            left_pointer += 1
        
array = [3,4,8,9,12,15,18]
target = 20
print(two_sum(array, target))