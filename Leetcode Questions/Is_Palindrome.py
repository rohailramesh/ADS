def is_palindrome(s):
    # first remove any whitespaces and non alpha numeric characters from string
    # convert string to lowercase
    # use two pointers - one at each end and move towards middle while checking if current value of both pointers match
    # return true if reached middle
    # s = ''.join(s.split()) #first splits all the words in list and then joins them on ''
    # can use isalnum() method to do it in one go
    s = ''.join(char for char in s if char.isalnum())
    s = s.lower()
    left_pointer, right_pointer = 0, len(s) - 1
    while left_pointer <= right_pointer:
        if s[left_pointer] != s[right_pointer]:
            return False
        left_pointer +=1
        right_pointer -=1
    return True
    print(left_pointer, right_pointer)
    print(s)
    
    

s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))