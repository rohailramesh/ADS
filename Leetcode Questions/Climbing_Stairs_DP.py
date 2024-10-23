# Climbing Stairs
# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.

# Example 1:

# Input: n = 2

# Output: 2
# Explanation:

# 1 + 1 = 2
# 2 = 2
# Example 2:

# Input: n = 3

# Output: 3
# Explanation:

# 1 + 1 + 1 = 3
# 1 + 2 = 3
# 2 + 1 = 3
# Constraints:

# 1 <= n <= 30

def climbingStairs(n):
    if n <= 3:
        return n
    n1, n2 = 2, 3

    for i in range(4, n + 1):
        temp = n1 + n2
        print(f'Current value of temp = {temp}')
        n1 = n2
        print(f'Current value of n1 = {n1}')
        n2 = temp
        print(f'Current value of n2 = {n2}')
    return n2
        

print(climbingStairs(5))