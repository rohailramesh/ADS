'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:
1 <= text.length <= 104
text consists of lower case English letters only.
'''


def number_of_balloons(str_input):
    word_dict = {}
    BALLOON = 'balloon'
    for char in str_input:
        if char in BALLOON:
            word_dict[char] = word_dict.get(char, 0)
    if any(char not in word_dict for char in BALLOON):
        return 0 # this is basically saying that if any of the character in string 'balloon' is not in the dict then return 0 as we need atleast 1 to work
    else:
        return min(word_dict['b'], word_dict['a'], word_dict['l'] // 2, word_dict['o'] // 2, word_dict['n']) # the //2 beside 'l' and 'o' is to get the most num of that char we can to make that str. eg: if input string has 4 l's then at most we can make the string balloon 2 times since 4 //2 is 2 but we still have to consider the remaining chars which is why we find the min from all of the chars
result = number_of_balloons("leetcode") 
print(result)    
