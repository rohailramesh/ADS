'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
'''

'''
Plan:
If either string is empty -> return false
Convert both strings to lowercase
Create a dict and store each chara as a key and value as 1
loop through the chars in second string and check if they are in dict
if all chars in dict then return true
else if char not in dict then return false

'''

# My attempt
def isAnagram1(string_s, string_t):
    if len(string_s) == 0 or len(string_t) == 0:
        return False
    string_s_lower = string_s.lower()
    string_t_lower = string_t.lower()
    string_dict = {}
    if len(string_s_lower) == len(string_t_lower):
        for char in string_s_lower:
            string_dict[char] = 1
        for char in string_t_lower:
            if char not in string_dict:
                return False
            return True
    else:
        return False

# Solution
'''
1. Return false if length of both strings are not equal
2. Convert both strings to lowercase and sort them
3. Return true if each element at index i is equal to other sorted string
''' 
def isAnagram2(string_s, string_t):
    if len(string_s) == 0 or len(string_t) == 0:
        return False
    string_s_lower = sorted(string_s.lower())
    string_t_lower = sorted(string_t.lower())
    if len(string_s_lower) == len(string_t_lower):
        for i in range(len(string_s_lower)):
            if string_s_lower[i] != string_t_lower[i]:
                return False
        return True
    return False


def isAnagram3(s,t):
    if len(s) != len(t):
        return False
    dict_s = {}
    dict_t = {}
    for i in range(len(s)):
        dict_s[s[i]] = 1 + dict_s.get(s[i],0)
        dict_t[t[i]] = 1 + dict_t.get(t[i],0)
    
    # for key,val in dict_s.items():
    #     print(key,val)
    # for key,val in dict_t.items():
    #     print(key,val)
    return dict_s == dict_t


string_s, string_t = 'hello', 'ellhi'
print(isAnagram3(string_s, string_t))