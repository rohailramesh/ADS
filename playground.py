fruits = {"apple", "banana", "kiwi", "mango", "apple", "orange"}
print(type(fruits))
print(fruits)

fruits_dict = {}
fruits_dict["apple"] = "apple"
fruits_dict["banana"] = "banana"
fruits_dict["mango"] = "mango"
print(type(fruits_dict))
print(fruits_dict)

ls = [x **2 for x in range(10)]
ls_1 = {x: x**2 for x in range(10)}
print(ls)

print(ls_1)

dict_name = dict(Rohail=21, Reeha=24, Rommel=26)
print(dict_name)

ls = [23,26,28]
for index, value in enumerate(ls):
    print(index, value)
    
pairs_ls = [(x,y) for x in [1,2,3] for y in [1,2,3] if x !=y]
print(pairs_ls)

res = []
for i in ([1,2,3]):
    for j in ([1,2,3]):
        if i != j:
            res.append((i,j))
print(res)    


ls = [2,3,6,8,9,11]
ls_2 = [x ** 2 if x % 2 == 0 else x for x in ls]
print(ls_2)

def matrices_1(matrix):
    row_len = len(matrix[0]) #the size of the first list inside the big list tells us the num of row
    col_len = len(matrix) #the size of the matrix itself tells us the num of cols
    print("Matrix dimensions are: ", row_len, "x", col_len)
    print(f"Matrix dimensions are: {row_len} x {col_len}")
    for row in range(row_len):
        for col in range(col_len):
            print(matrix[row][col], end=" ")
        print()


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrices_1(matrix)