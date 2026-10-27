class Solution(object):
    def createGrid(self, m, n):
        grid = ["." * n]
        for i in range(1, m):
            to_add = ("#" * (n - 1)) + "."
            grid.append(to_add)

        return grid