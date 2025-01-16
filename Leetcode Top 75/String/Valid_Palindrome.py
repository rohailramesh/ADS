# This uses the two pointer technique
'''
Valid Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.

'''

def validPalindrome(string):
    n = len(string)
    L = 0
    R = n -1
     
    while L < R: #not doing equals to because whe we get both pointers to the middle we know it will be same anywyas so no need to check 
        # print(L,R)
        if not string[L].isalnum(): #if current value at left pointer is not alphanumerical then it just shifts that pointer
            L += 1
            continue
        if not string[R].isalnum():#same here for right pointer
            R -= 1
            continue
        # once both pointer values are in format we want, we can now check if they are equal to each other not and if they are not equal then we return false
        if string[L].lower() != string[R].lower():
            return False
        L += 1
        R -= 1
    return True
print(validPalindrome("wasitacaroracatisaw"))