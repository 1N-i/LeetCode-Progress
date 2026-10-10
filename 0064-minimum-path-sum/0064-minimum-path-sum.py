class Solution(object):
    def minPathSum(self, grid):
        for collumn in range(1, len(grid[0])):
            grid[0][collumn] += grid[0][collumn-1]

        for row in range(1, len(grid)):
            grid[row][0] += grid[row-1][0]

        for y in range(1, len(grid)):
            row = grid[y]
            for x in range(1, len(row)):
                row[x] += min(grid[y-1][x], row[x-1])

        return grid[-1][-1]