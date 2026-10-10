class Solution(object):
    def minPathSum(self, grid):
        for y in range(len(grid)):
            row = grid[y]
            for x in range(len(row)):
                if x == 0 and y == 0:
                    continue
                elif y == 0:
                    grid[0][x] += grid[0][x-1]
                    continue
                elif x == 0:
                    grid[y][0] += grid[y-1][0]
                    continue

                row[x] += min(grid[y-1][x], row[x-1])

        return grid[y][x]