'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
 
Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
'''

# creating a binary tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


'''
Plan: 
Do a depth first search pre-order traversal - recursive
Find the max from left and right sub tree traversal and add 1 for the node
'''

def maxDepth(root):
    if not root:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return 1 + max(left, right)
# Time complexity is O(n)
# Space complexity is O(h)


def maxDepthIterative(root):
    '''
    start by having a stack to which we will add the current node and its depth (level)
    then we can look at its left and right children if there is any and add that and its depth too
    we can pop of the parent node as we move down the depth and update our stack
    once we reach to the leaf node, we can then return the depth as that will be the max depth
    '''
    if not root:
        return 0
    stack = [[root, 1]] # we will store the root and its level initially in stack
    res = 1 # since our tree is not empty, we have added the root and its level which is 1 to the stack so we know that for now the max depth (answer) is 1 so we can assign that to the variable res for now and update as we go
    
    # a while loop until our stack is not empty (if it was empty that means we have reached to the leaf nodes and can return our res now)
    while stack:
        node, depth = stack.pop() #this is to start removing the node once it is processed and move to its children left and right node
        if node: #only working on nodes that have left and right
            res = max(res, depth) #updating the res with the max from current val of res or the value of depth (level of the node)
            # now we append the left and right nodes to stack along with their depth
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res
# Example
root = TreeNode("3")
node_9 = TreeNode("9")
node_20 = TreeNode("20")
node_15 = TreeNode("15")
node_7 = TreeNode("7")

root.left = node_9
root.right = node_20
node_20.left = node_15
node_20.right = node_7

print(maxDepth(root))
print(maxDepthIterative(root))