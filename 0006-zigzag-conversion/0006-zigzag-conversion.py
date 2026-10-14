class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s): return s

        grid = [""] * numRows
        row = 0
        direction = 1
        for l in s:
            grid[row] += l
            row += direction
            if row == numRows - 1:
                direction = -1
            elif row == 0:
                direction = 1

        return "".join(grid)