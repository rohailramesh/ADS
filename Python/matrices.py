def matrices_1(matrix):
    row_len = len(matrix[0]) #the size of the first list inside the big list tells us the num of row
    col_len = len(matrix) #the size of the matrix itself tells us the num of cols
    print("Matrix dimensions are: ", row_len, "x", col_len)
    print(f"Matrix dimensions are: {row_len} x {col_len}")
    matrix[0][-1] = "Heee" #accessing a specific value in matrix and changing it
    for row in range(row_len):
        for col in range(col_len):
            print(matrix[row][col], end=" ")
        print()

# Program to add two matrices using nested loop
matrix_a = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def add_matrices(matrix_a, matrix_b):
    for row in range(len(matrix_a)):
        for column in range(len(matrix_a[0])):
            result[row][column] = matrix_a[row][column]+ matrix_b[row][column] #this uses a new matrix (list of list) to store the results meaning it has a space complxity of O(n)
    for r in result:
        print(r)

add_matrices(matrix_a, matrix_b)

def matrix_multiplication(matrix_a, matrix_b):
    result = []
    matrix_a_row = len(matrix_a[0])
    matrix_a_col = len(matrix_a)
    matrix_b_row = len(matrix_b[0])
    matrix_b_col = len(matrix_b)
    
    for row in range(matrix_a_row):
        for col in range(matrix_a_col):
            result.append(row * col)
    print(result)


matrix_a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix_b = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# matrices_1(matrix)

# matrix_multiplication(matrix_a, matrix_b)