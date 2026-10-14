class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1: return s

        grid = [[] for _ in range(numRows)]

        row = 0
        direction = 1
        for l in s:
            grid[row].append(l)
            row += direction
            if row == numRows - 1:
                direction = -1
            elif row == 0:
                direction = 1

        ans = ""
        for word in grid:
            ans += "".join(word)

        return ans