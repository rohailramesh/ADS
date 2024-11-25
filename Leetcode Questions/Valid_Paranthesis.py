'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

'''

'''
Plan:
- Data structure to use: stack
- For each char in string s, if char is opening char then add in stack
- If stack is empty return true
- Check if string is valid or not
    - if current char is a closing paranthesis but stack[-1] is not the corressponding opening paranthesis then return false as it is not valid string
    - else pop the top element in stack since there is a matching paranthesis
- return not stack (if all paranthesis matched then it is valid and returns true)
'''

def valid_paranthesis(paranthesis_string):
    stack = []
    for char in paranthesis_string:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or \
                (char == ")" and stack[-1] != "(") or \
                (char == "}" and stack[-1] != "{") or \
                (char == "]" and stack[-1] != "["):
                    return False
            stack.pop()
    return not stack #if stack is empty then all paranthesis match and returns true
        
            
paranthesis_string = "({{})"
print(valid_paranthesis(paranthesis_string))