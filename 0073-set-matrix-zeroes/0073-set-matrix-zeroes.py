class Solution(object):
    def setZeroes(self, matrix):
        xs, ys = set(), set()
        len_x, len_y = len(matrix), len(matrix[0])
        for x in range(len_x):
            for y in range(len_y):
                if matrix[x][y] == 0:
                    xs.add(x)
                    ys.add(y)

        for x in xs:
            for y in range(len_y):
                matrix[x][y] = 0

        for y in ys:
            for x in range(len_x):
                matrix[x][y] = 0