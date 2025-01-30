'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''
# This is row wise traversal
def set_matrix_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j])

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_matrix_zeros(matrix))


def set_matrix_zeros(matrix):
    pass