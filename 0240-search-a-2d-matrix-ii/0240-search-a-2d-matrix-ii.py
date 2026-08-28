class Solution(object):
    def searchMatrix(self, matrix, target):
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            look = matrix[row][col]
            if look == target: return True
            elif look < target: row += 1
            else: col -= 1

        return False