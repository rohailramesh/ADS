# In order traversal is also a kind of depth first search that traverses a binary tree in a specifc order. 
# It traverses the left sub tree until there is a node. Once it reaches to end, it processes that node data and moves back to parent node which is then procesed before moving to right subtree. This is done iteratively/recursively

class TreeNode:
    # Creating a Node class which will initialise the data with the data passed and a left and right node set to none initially
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode("1")
nodeA = TreeNode("2")
nodeB = TreeNode('3')
nodeC = TreeNode('4')
nodeD = TreeNode('5')

root.left = nodeA
root.right = nodeD
nodeA.left = nodeB
nodeA.right = nodeC



# In-order using recursion
def in_order_recursively(root):
    res = []
    def in_order_helper(root):
        if not root:
            return
        in_order_helper(root.left)
        res.append(root.data)
        in_order_helper(root.right)
    in_order_helper(root)
    return res

print("This is in_order recursively: ", in_order_recursively(root))


# In-order using iteration
def in_order_iteratively(root):
    res = []
    stack = []
    current_node = root
    # while loop until stack or pointer is not empty/null
    while stack or current_node:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        res.append(current_node.data)
        current_node = current_node.right
    return res

print("This is in_order iteratively: ", in_order_iteratively(root))