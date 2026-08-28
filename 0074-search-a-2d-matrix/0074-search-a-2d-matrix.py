class Solution(object):
    def searchMatrix(self, matrix, target):
        up, down = 0, len(matrix) - 1
        while up <= down:
            mid_row = (up + down) // 2

            left, right = 0, len(matrix[mid_row]) - 1
            while left <= right:
                mid_col = (left + right) // 2
                look = matrix[mid_row][mid_col]

                if look == target: return True
                elif look < target: left = mid_col + 1
                else: right = mid_col - 1

            if look < target: up = mid_row + 1
            else: down = mid_row - 1

        return False