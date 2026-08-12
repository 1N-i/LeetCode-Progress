class Solution(object):
    def rotate(self, matrix):
        row, col = len(matrix), len(matrix)

        for x in range(row):
            for y in range(x + 1, col):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        for row in range(row):
            matrix[row].reverse()