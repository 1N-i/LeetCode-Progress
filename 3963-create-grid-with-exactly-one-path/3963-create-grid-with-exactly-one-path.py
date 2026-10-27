class Solution(object):
    def createGrid(self, m, n):
        grid = ["." * n]
        for i in range(1, m):
            to_add = "#" * n
            add = list(to_add)
            add[-1] = "."
            grid.append("".join(add))

        return grid