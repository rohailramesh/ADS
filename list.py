# list comprehension
# creating an array of length 5. value is current value of i as it runs a for loop of length 5
arr = [i for i in range(5)]
print(arr)


# creating a 2d list -> inner loop creates an array of length 4 with 0 as each value and then outer loop multiples that by 4
arr = [[0] * 4 for i in range(4)]
print(arr)

twoD_arr = [[4] * 4 for i in range(4)]
print(twoD_arr) 