'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

def num_of_islands(grid):
    # return if grid is empty
    if not grid:
        return
    # get row and col of grid
    row, col = len(grid), len(grid[0])
    # print(row,col)
    
    # helper function to run dfs to traverse grid and mark islands
    def dfs_helper(x, y):
        # if current point in grid at coord x and y is out of range or not 1 then return
        if(x < 0 or x >= row) or \
            (y < 0 or y >= col) or \
                grid[x][y] != "1":
                    return
        # if current value at coord x,y is 1, change to 0
        grid[x][y] = 0
        
        # Recursively explore adjacent points
        dfs_helper(x+1, y)
        dfs_helper(x-1, y)
        dfs_helper(x, y+1)
        dfs_helper(x, y-1)
    
    islands_counted = 0
    # traverse through each point on grid and use the dfs helper to mark islands and increment islands_counted
    for x in range(row):
        for y in range(col):
            if grid[x][y] == "1":
                islands_counted += 1
                dfs_helper(x,y)
    return islands_counted


grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(num_of_islands(grid))