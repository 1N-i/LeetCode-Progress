class Solution(object):
    def countNegatives(self, grid):
        ans = 0
        for level in grid:
            for num in sorted(level):
                if num < 0: ans += 1
                else: break

        return ans