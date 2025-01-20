'''
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

def container_with_most_water_optimised(height_ls):
    max_area = 0
    pointer_left = 0
    pointer_right = len(height_ls) - 1
    while pointer_left < pointer_right:
        height = min(height_ls[pointer_left], height_ls[pointer_right]) 
        width = pointer_right - pointer_left
        area = height * width
        max_area = max(area, max_area)
        if height_ls[pointer_left] < height_ls[pointer_right]:
            pointer_left += 1
        else:
            pointer_right -= 1
    return max_area

height_ls = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water_optimised(height_ls))


def container_with_most_water_brute_force(height_ls):
    '''
    This is brute force approach that has time complexity of n^2 
    Idea is to try every possible combination using two pointer
    One pointer at height[i] and other at height[i+1]
    Find the area of the values at those two pointers and update if necessary to find the max and return the area
    '''
    res = 0
    for i in range(len(height_ls)):
        for j in range(i+1, len(height_ls)):
            height = min(height_ls[i], height_ls[j])
            width = j - i
            area = width * height
            res = max(res, area)
    return res

height_ls = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water_brute_force(height_ls))