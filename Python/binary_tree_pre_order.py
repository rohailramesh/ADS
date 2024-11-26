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

def preOrderTraversalRecursively(node): #using recursion which automatrically handles back tracking to parent node
    if node is None:
        return
    print(node.data, end=" ")
    preOrderTraversalRecursively(node.left)
    preOrderTraversalRecursively(node.right)

preOrderTraversalRecursively(root)

def preOrderTraversalIteratively(node): #using iteration to handle the back tracking manually
    currentNode = root
    tempStack= []
    traversedTreeArray = []
    while currentNode or tempStack:
        if currentNode:
            traversedTreeArray.append(currentNode.data)
            tempStack.append(currentNode.right)
            currentNode = currentNode.left
        else:
            currentNode = tempStack.pop()
    return traversedTreeArray
            

print(preOrderTraversalIteratively(root))
'''
Example
        1
       / \
      2   3
     / \
    4   5
    
Starting Point:

currentNode = 1
tempStack = []
traversedTreeArray = []
Step-by-Step Execution:

Visit 1 → Add 1 to traversedTreeArray.
Stack: [3] (push right child). Move to 2 (left child).
Visit 2 → Add 2 to traversedTreeArray.
Stack: [3, 5] (push right child). Move to 4 (left child).
Visit 4 → Add 4 to traversedTreeArray.
Stack: [3, 5]. No left child → Backtrack using the stack.
Backtrack → Pop 5 from stack.
Visit 5 → Add 5 to traversedTreeArray.
Stack: [3]. No left child → Backtrack again.
Backtrack → Pop 3 from stack.
Visit 3 → Add 3 to traversedTreeArray.
Stack: []. No left child.
Final Result: traversedTreeArray = [1, 2, 4, 5, 3]
    
'''