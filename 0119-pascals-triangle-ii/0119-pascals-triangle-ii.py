class Solution(object):
    def getRow(self, rowIndex):
        triangle = []
        for row_size in range(rowIndex + 1):
            triangle_row = [0] * (row_size + 1)

            if row_size > 1:
                for i in range(len(triangle_row) - 1):
                    triangle_row[i] = triangle[-1][i] + triangle[-1][i - 1]

            triangle_row[0], triangle_row[-1] = 1, 1
            triangle.append(triangle_row)

        return triangle[-1]