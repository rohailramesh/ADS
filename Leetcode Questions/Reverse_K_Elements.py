'''
Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

enqueue(x) : Add an item x to rear of queue
dequeue() : Remove an item from front of queue
size() : Returns number of elements in queue.
front() : Finds front item.

'''

'''
Plan:
Data structure to use: Stack and Queue
- if k is greater than length of queue, return
- for loop for k elements:
    - dequeue the first element in queue and append to a stack. repeat this for k elements
- then pop the element from stack and append it to the end of queue.
- finally deque the length of queue - k elements items and enqueue it in the same array so they go back to the original position and everything comes into the right place
'''

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def printStack(self):
        # for i in range(self.size()):
        #     print(self.stack[i])
        print(self.stack)

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def printQueue(self):
        print(self.queue)
def reverse_k_elements(queue, k):
    if k > queue.size():
        return queue
    tempStack = Stack()
    for _ in range(k):
        tempStack.push(queue.dequeue())
    while not tempStack.isEmpty():
        queue.enqueue(tempStack.pop())
    for _ in range(queue.size() - k):
        queue.enqueue(queue.dequeue())
    return queue
    
        


# Test case
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
k = 3
result = reverse_k_elements(queue, k)
result.printQueue()