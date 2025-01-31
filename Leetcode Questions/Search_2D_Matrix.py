'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity
 
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
'''

# binary search will only work when the list is ascending order
# time complexity of O log(n)
# space complexity of O (1)

# Using the idea of binary search to solve this problem
# def binary_search(nums, target):
#     left_pointer = 0
#     right_pointer = len(nums) - 1
#     while left_pointer <= right_pointer:
#         mid = (left_pointer + right_pointer) // 2
#         if nums[mid] == target:
#             return True
#         elif nums[mid] > target:
#             right_pointer = mid - 1
#         elif nums[mid] < target:
#             left_pointer = mid + 1
#     return False

# nums = [4,7,8,11,13,15]
# target = 133
# print(binary_search(nums, target))

'''
We want to imagine the matrix as a flat list and assign each number a temp index from 0 to n-1 where n is the length of the list. Then we perform binary search on that flat list and check if our target is in the list or not

How will I update the value of the middle var especially when thinking that the matrix is a flat list and not 2D?
- For list[i][j] this is how to find i and j using the temp index from earlier:
- i is the row index value and it can be found by Middle // num_of_cols
- j is the column index value and it can be found by Middle % num_of_cols
'''

def search_2d_matrix(nums_matrix, target):
    num_of_rows = len(nums_matrix)
    num_of_cols = len(nums_matrix[0])
    total_nums_in_matrix = num_of_rows * num_of_cols
    left_pointer = 0
    right_pointer = total_nums_in_matrix - 1
    
    while left_pointer <= right_pointer:
        middle = (left_pointer + right_pointer) // 2
        row = middle // num_of_cols
        col = middle % num_of_cols
        middle_num = nums_matrix[row][col]
        if middle_num == target:
            return True
        elif target > middle_num:
            left_pointer = middle + 1
        else:
            right_pointer = middle - 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 32

print(search_2d_matrix(matrix, target))

# This solution has the time complexity of O log(n * m)