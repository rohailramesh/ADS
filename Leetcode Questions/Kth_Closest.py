# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
import heapq
def kClosest(points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    # Find distance for each point
    # Add distance, points to list as an element
    # Heapify list
    # Pop element from heap for k times
    # Return the points of popped element
    
    distances = []
    res = []
    for x, y in points:
        dist = (x**2) + (y**2)
        distances.append([dist, x, y])
    # print(distances)
    heapq.heapify(distances)
    while k > 0:
        dist, x, y = heapq.heappop(distances)
        res.append([x,y])
        k -= 1
    return res

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))