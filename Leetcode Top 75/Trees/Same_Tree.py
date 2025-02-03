'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 
Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 10^4
'''

# PLan is to use depth first search recursively and check if the structure of both trees are same and also the values at current node

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSameTree(tree_1, tree_2):
    # if both nodes are None they are same
    if not tree_1 and not tree_2:
        return True
    
    # if one tree is empty but other is not then they are not the same trees
    if (tree_1 and not tree_2) or (not tree_1 and tree_2):
        return False
    
    # if both trees have a node we check if the value of the both nodes are same
    if tree_1.data == tree_2.data:
        return isSameTree(tree_1.left, tree_2.left) and isSameTree(tree_1.right, tree_2.right)
    
    # finally values are not same and structure is not same too
    return False 


'''
Approach
Check the base case: if both trees are null, return true.
Check if only one tree is null or the values of the current nodes are different, return false.
Recursively check if the left subtrees of both trees are identical.
Recursively check if the right subtrees of both trees are identical.
Return the logical AND of the results from steps 3 and 4.
Complexity

Time complexity:
The time complexity of the solution is O(min(N,M)), where N and M are the number of nodes in the two trees, respectively. This is because we need to visit each node once in order to compare their values. In the worst case, where both trees have the same number of nodes, the time complexity would be O(N).

Space complexity:
The space complexity of the solution isO(min(H1,H2)), where H1 and H2 are the heights of the two trees, respectively. This is because the space used by the recursive stack is determined by the height of the smaller tree. In the worst case, where one tree is significantly larger than the other, the space complexity would be closer to O(N) or O(M), depending on which tree is larger.
'''