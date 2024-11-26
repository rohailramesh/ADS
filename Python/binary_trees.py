# Binary trees have a root or the parent node and two children - left and right which are nodes (lead nodes)
# The size of the tree is the total number of nodes in the binary tree
# The height of the binary tree is the total number of edges (lines) from root node to leaf node
# Binary trees have a non-linear data structure as compared to arrays and linked lists

# BInary trees are preferred over arrays or linked lists


'''
Types of binary trees:
- Balanced -> The height between left and right subtree for each node at most be one

- Complete -> All levels of tree have full nodes excpet the last level where all the leaf nodes are. Thet can be full or if not possible then atleast filled from left to right. This is also a balanced tree

- Full -> Tree where a parent node has 0 or 2 children node not 1. Does not have to be balanced or complete

- Perfect -> tree that is balanced, complete and full
'''

# Binary tree implementation
class TreeNode:
    # Creating a Node class which will initialise the data with the data passed and a left and right node set to none initially
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB
nodeA.left = nodeC
nodeA.right = nodeD
nodeB.left = nodeE
nodeB.right = nodeF
nodeF.left = nodeG

# Test
print("root.right.left.data:", root.right.left.data)

# Traversing binary trees
'''
Type 1 -> pre-order

Type 2 -> in-order

Type 3 -> post-order
'''

