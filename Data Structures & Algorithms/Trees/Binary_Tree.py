# In binary seearch trees, the left child is less than the root and the right child is greater than the root

# Size of the tree is the total number of nodes in the tree
# Height of the tree is the number of edges in the longest path from the root to a leaf

# creating a binary tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
# Using pre-order depth first search to traverse a binary tree  
def pre_order_traversal(root):
    if root is None:
        return
    print(root.data, end=", ")
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)

root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
root.left = nodeA
root.right = nodeB
nodeA.left = nodeC
nodeA.right = nodeD
nodeB.left = nodeE

print(root.left.left.data)
pre_order_traversal(root)



