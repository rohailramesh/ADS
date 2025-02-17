'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''

'''
Plan:
This problem will use a sliding window approach along with a list to keep count of how many times an uppercase letter is used like a counter
The aim is to move the window across the string until the largest sequence is found using pointer A and B. If the window is not valid (doesn't work with k) then update the pointers
'''
 
def character_replacement(s, k):
    longest_sequence_len = 0 #This is the final answer (which will be updated)
    left_pointer = 0 #pointer 1 that starts at the very start of string
    char_dict = [0] * 26 #creating a list to keep count of which char is used
    for right_pointer in range(len(s)): #second pointer that will move through string in the loop of length string
        char_dict[ord(s[right_pointer])-65] += 1 #updating the count of char in the list by getting the ascii value of value at right pointer as that could be part of longest sequence
        while (right_pointer - left_pointer + 1) - max(char_dict) > k:
            char_dict[ord(s[1])-65] -= 1
            left_pointer += 1
        # this while loop checks if the current window is valid or not and if it has exceeded the k limit
        # if that is the case, then decrement the count and move the left pointer to the right so now looking at the new value
        longest_sequence_len = max(longest_sequence_len, (right_pointer - left_pointer + 1)) #find the max from previous longest sequence and the new window now and update the longest sequence
    return longest_sequence_len

test1 = "ABBA"
k = 2
print(character_replacement(test1, k)) 