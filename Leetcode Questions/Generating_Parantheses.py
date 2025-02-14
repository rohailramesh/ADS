'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:
1 <= n <= 8
'''

'''
Plan =>
- If n is the total number of well formed paratheses to generate then, i should have n * 2 parantheses (open and close)
- If open_parantheses == close_parantheses == n: then we have the parantheses we need
- Using a stack we can update the open or closing paran through recursive backtracking and check if open paran is always there before closing
- if num_of_closing_paran is less than num_of_open_paran then we add closig paran
'''

def generate_parantheses(n):
    res = []
    stack = []
    
    def recursive_backTracking(open_paran, close_paran):
        if open_paran == close_paran == n:
            res.append("".join(stack))
            return
        if open_paran < n:
            stack.append("(")
            recursive_backTracking(open_paran + 1, close_paran)
            stack.pop()
        if close_paran < open_paran:
            stack.append(")")
            recursive_backTracking(open_paran, close_paran + 1)
            stack.pop()
    recursive_backTracking(0,0)
    return res

n_1 = 3
print(generate_parantheses(3))

# Time complexity: O(2^n)
# Space complexity: O(n)