# Prefix sum helps compute cumulative sums over an array. So instead of computing the sum for a givenn range/index everytime, it computes it once and then can be used to compute other sums.

# eg: array = [1,2,3,4,5]. to find the prefix_sum you take previous value in array and add it to current value [1,3,6,9,13,18]

numbers = [2, 3, 7, 1, 8]

# Step 1: Create a prefix sum list
prefix_sum = [0] * len(numbers)  # Initialize a list of the same size as `numbers`

# Step 2: Fill in the prefix sum list
prefix_sum[0] = numbers[0]  # The first element is the same
for i in range(1, len(numbers)):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i]

print("Original list:", numbers)
print("Prefix sum list:", prefix_sum)

def range_sum(i, j):
    if i == 0:
        return prefix_sum[j]
    return prefix_sum[j] - prefix_sum[i - 1]

print(range_sum(1, 3)) 
