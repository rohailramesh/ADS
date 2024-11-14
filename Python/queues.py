# Queues are similar to Stacks but they operate on the principle of first in first out - FIFO
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element): #add at start of list
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0) #remove the first element from list - FIFO
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", myQueue.queue)

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())


# Using linked list to implement a queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None # front of the queue
        self.rear = None # rear of the queue
        self.length = 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None: # if queue is empty
            self.front = self.rear = new_node # set front and rear to new node
            self.length += 1 # increment length
            return
        self.rear.next = new_node # if queue is not empty then point the next pointer of rear to new node
        self.rear = new_node # set rear to new node
        self.length += 1 # increment length
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front # store the front of the queue in temp
        self.front = temp.next # point the front to the next node of the front 
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")
myQueue.printQueue()

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())