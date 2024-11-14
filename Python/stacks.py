# data sructure which can hold many elements. The main idea is that the last element inserted into the stack will be the first element out when popped


# you can push an element into a stack
# you can pop an element into a stack
# you can peek at the top element in the stack
# you can check if the stack is empty
# you can check the size of the stack


# To implement a stack, youc an use an array or a linked list

stack = []

# pushing into the stack
stack.append('A')
stack.append('B')
stack.append('C')

# print(stack)
# Result -> [A,B,C]
# A was the first element pushed into the stack so it is the last element in the stack


stack.pop()
# print(stack)
# Result -> [A,B]
# The last element will pop from the array but in a stack that is the very first element at the top becuase of 'last in first out' principle 


topElement = stack[-1]
# print(topElement)

isEmpty = not bool(stack)
# print(isEmpty)

# print(len(stack))


# ---------------------------------------------------------------
# creating a class for stacks using an array
class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return
        self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
        
myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
print(myStack.stack)
print(myStack.peek())
print(myStack.pop())
print(myStack.size())
print(myStack.isEmpty())


# implementing stack using linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    # new node created
    # if stack has items -> point the next pointer of new node to current top item
    # update the head with new node
    # increase size of stack by 1
    def push(self, value):
        new_node = Node(value)
        if self.head: # if stack is not empty
            new_node.next = self.head # point the next pointer of new node to current top item
        self.head = new_node # update the head with new node
        self.size += 1
        
    
    def pop(self):
        if self.isEmpty():
            return
        pop_node = self.head
        self.head = self.head.next
        self.size -= 1
        return pop_node
    
    def peek(self):
        if self.isEmpty():
            return
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def size(self):
        return self.size
    

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())