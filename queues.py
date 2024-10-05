# These are double ended queues
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)
queue.appendleft(3)
print(queue)
queue.popleft() #this is done in constant time because it always pops the veryfirst value from left

# queue is different from list becuase queue has a structure of double linked list meaning it is accessible from both sides as compared to a list. Therefore the time complexity to pop from left or right hand side is of constant time but to pop or remove 