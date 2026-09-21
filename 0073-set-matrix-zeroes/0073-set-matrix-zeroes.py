class Solution(object):
    def setZeroes(self, matrix):
        guide = { "0": [] }
        len_x, len_y = len(matrix), len(matrix[0])
        for x in range(len_x):
            for y in range(len_y):
                if matrix[x][y] == 0:
                    guide["0"].append([x, y])

        xs, ys = [], []
        for pair in guide["0"]:
            xs.append(pair[0])
            ys.append(pair[1])

        for x in xs:
            for y in range(len_y):
                matrix[x][y] = 0

        for y in ys:
            for x in range(len_x):
                matrix[x][y] = 0