class Solution(object):
    def countNegatives(self, grid):
        ans = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] < 0:
                    ans += 1

        return ans