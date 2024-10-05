# Data structure to find min and max of set of values - impleemnted as arrays

import heapq

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 0)
heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 1)
print(minHeap) #by default heaps are min heaps so they are displayed from min to max
print(minHeap[0]) #so the min will always be at the 0th index


# can pop from min heaps too

# to work with max heaps use a min heap but for each element multiply it by -1 when pushing to heap or pooping it and that way max will always be at index 0. Make sure to multiply it by -1 again when accessing elements from heap since they will be negative

maxsHeap = []
heapq.heappush(maxsHeap, -3)
heapq.heappush(maxsHeap, -6)
heapq.heappush(maxsHeap, -4)
heapq.heappush(maxsHeap, -1)

print(maxsHeap)
print(-1 * maxsHeap[0])


# popping the max element from heap through while loop until all are popped
while len(maxsHeap):
    print(-1 * heapq.heappop(maxsHeap))
    print(maxsHeap)    
    
# building a heap from initial array of values
arr = [6,1,9,2]
heapq.heapify(arr)
print(arr)