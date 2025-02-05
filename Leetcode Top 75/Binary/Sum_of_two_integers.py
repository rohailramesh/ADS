'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5
 

Constraints:
-1000 <= a, b <= 1000
'''

'''
Plan: Using bit manipulation, I will find the sum with the help of xor and and operators
1. find xor of a and b
2. find a AND b which is the carry and assign it to b
3. shift the a AND b result to the left by 1
4. repeat iteration until b is not 0 meaning no carry left
5. return a which is the sum

Since this solution is in python, to deal with large numbers that use more bits to represent a value unlike other languages, use the masking technique

Masking ensures that Python is forced to work like a normal 32 bit computer. So when working with large negative numbers, instead of counting beyond 32 bits, it just stops and doesn't count any further.
'''


def getSum(a,b):
    # 32 bit mask in hexadecimal
    mask = 0xffffffff
    while (b & mask > 0):
        carry = (a & b) << 1
        a = (a ^ b)
        b = carry
    if b > 0:
        return (a & mask)
    else:
        return a
    
print(getSum(10,3))

print(10 & 3)