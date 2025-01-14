'''
Non-Cyclical Number
A non-cyclical number is an integer defined by the following algorithm:

Given a positive integer, replace it with the sum of the squares of its digits.
Repeat the above step until the number equals 1, or it loops infinitely in a cycle which does not include 1.
If it stops at 1, then the number is a non-cyclical number.
Given a positive integer n, return true if it is a non-cyclical number, otherwise return false.

Example solution -> https://www.youtube.com/watch?v=ljz85bxOYJ0
'''

def non_cyclical_number(num):
    num_set_tracker = set() 
    while num not in num_set_tracker: #add each current num to set until there is a duplicate (since set only have unique values) 
        num_set_tracker.add(num)
        num = findSumOfSquares(num) #update the current value of num by calculating sum of squares through helper function
        # print(num)
        if num == 1: #if at any point num is 1 return true as we have found happy number
            return True
    return False 
          
def findSumOfSquares(num): #helper function to calculate sum of square
    sum = 0
    while num:
        digit = num % 10 #finds the last digit in the input num 
        digit = digit ** 2 #takes that last digit and sqaures it and adds to temp sum
        sum += digit
        num = num // 10 #updates the digit value
    return sum 


print(non_cyclical_number(19))