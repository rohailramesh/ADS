# heaps and priority queues are pretty much interchangeable
# by default heaps are min heaps when using the heapq module

import heapq
A = [5,1,2,9,3,6,0,-2,7,-5,4,2]
heapq.heapify(A) # min heapifies the list. time complexity is O(n)
print(A)

# heappeek is peeking at the min element in heap without having to pop it. this is in constant time complexity
print(A[0])

# Another way to find the min in min heap is by popping it since it will pop the most min element there is. Also maintains the heap strucutre after the pop
heapq.heappop(A)
print(A)

# Heappush pushes the element at end of heap 
heapq.heappush(A, -3)
heapq.heapify(A)
print(A)


# heap sort is one of the most efficient sort (sorted asc by default). Time complexity is nlogn and Space complexity is O(n)
def heapSort(arr):
    heapq.heapify(arr)
    sorted_heap = [0] * len(arr)
    for i in range(len(arr)):
        min_heap = heapq.heappop(arr)
        sorted_heap[i] = min_heap
        print(sorted_heap)

arr = [1,3,5,7,9,2,4,6,8,0]
# heapSort(arr)

# since heaps are min heaps by default, to work with max heaps, just neegate the values at start by changing their signs. When returning an answer just negeate them again to get original element
B = [-4,3,1,0,2,5,10,8,12,9]
for i in range(len(arr)):
    B[i] = -B[i]

heapq.heapify(B) #map heap
print(B)



        
