'''
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
Plan:
First check for base case -> return root if no root
Then assign root.left to root.right and root.right to root.left (basically switching them around)
Then repeat this process recursively on the sub tree
Return the node 
'''

def invertTree(root):
    if not root:
        return root
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

# Time complexity of O(n) where n is the number of nodes
# Space complexity is O(h) where h is the height of the tree which can also be O(n) since the tree could be as long as the number of nodes