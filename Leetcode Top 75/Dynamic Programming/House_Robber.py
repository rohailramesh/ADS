# - House Robber - https://leetcode.com/problems/house-robber/
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

'''

'''
This problem has multiple ways in which it can be solved
1. Recursion with a time and space complexity of O(2^n) and space O(n)
2. Top down approach using memoisation Time and space complexity of O(n)
3. Bottom Up Dynamic Approach (Tabulation) using O(n) space and time complexity of O(n). Using for loops instead of recursion
4. Bottom Up Dynamic Approach using constant space and time complexity of O(n)
'''

# Main logic to solve this problem that is common in all 4 approaches above:
'''
If there is only one house to rob then the value of that house is instantly returned
If there is two houses to rob then find the max out of those two and return that. This is becuase they are adjacent so we can't rob both

If there is more then two houses adn you can't rob adjacent houses:
find the current house plus the value of houses two positions back and then find the value of one house back from current position
Return which ever is the max 

'''


# 1. Recursion with a time and space complexity of O(2^n) and space O(n)
def house_robber_recursion(houses):
    n = len(houses)
    def helper(i):
        if i == 0:
            return houses[0]
        if i == 1:
            return max(houses[0], houses[1])
        return max(houses[i]+ helper(i-2), helper(i-1))
    return helper(n-1)




# 2. Top down approach using memoisation Time and space complexity of O(n)
def house_robber_memoisation(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    memo = {0: nums[0], 1:max(nums[0], nums[1])}
    def helper(i):
        if i in memo:
            return memo[i]
        else:
            memo[i] = max(nums[i]+helper(i-2), helper(i-1))
            return memo[i]
    return helper(n-1) #returns the last value in memo as that is the total value robbed


#  3. Bottom Up Dynamic Approach (Tabulation) using O(n) space and time complexity of O(n). Using for loops instead of recursion

def house_robber_dp_approach(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(nums[i] + dp[n-2], dp[i-1])
    return dp[n-1]


# 4. Bottom Up Dynamic Approach using constant space and time complexity of O(n)
def house_robber_dp_optimised_approach(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    prev = nums[0]
    curr = max(nums[0], nums[1])
    for i in range(2, n):
        prev = curr
        curr = max(nums[i] + prev, curr)
    return curr