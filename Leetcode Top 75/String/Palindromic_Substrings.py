'''
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.


Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
'''

'''
Plan:
Loop through the string and let each char be the middle in the loop
Have left and right pointer point to middle which then move outwards while being in bound - this is to cover the odd length palindromes
Have left pointer point to middle value and right pointer to middle + 1 in the loop - to cover all the even palindromes
'''

def find_plaindromic_substrings(str):
    res = 0
    def find_palindrome_helper(str, left_pointer, right_pointer):
        count = 0
        while left_pointer >= 0 and right_pointer < len(str) and str[left_pointer] == str[right_pointer]:
            count += 1
            left_pointer -= 1
            right_pointer += 1
        return count
    
    for i in range(len(str)):
        res += find_palindrome_helper(str, i, i) #for odd lengths of palindrome
        res += find_palindrome_helper(str, i, i+1) #for even lenghts of palindrome
    return res

str = 'aaa'
print(find_plaindromic_substrings(str))

# This solution has the time complexity of O (n^2) and time complexity of O (n)