'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

'''
Plan:
This is basically a Breadth First Search Algorithm
Idea is to add the node(s) at each level into the queue and then pop from left while running a loop that has a length of the number of nodes in that level. As you pop from left, add that node value to a list for that level
Continue till all levels are visited and then merge all the level lists into a single list and return it. Do this until q is not empty and within the loop itself, check if there are any nodes or level that are empty before adding to list.
'''
from collections import deque
class TreeNode:
    def __init__(self, left, right, val=0):
        self.left = None
        self.right = None
        self.val = val

def levelOrder(root):
    res = []
    queue = deque()
    queue.append(root) #very first node in tree
    while queue:
        len_of_queue = len(queue)
        tree_level = []
        for _ in range(len_of_queue):
            node = queue.popleft()
            if node:
                tree_level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if tree_level:
            res.append(tree_level)
    return res
    