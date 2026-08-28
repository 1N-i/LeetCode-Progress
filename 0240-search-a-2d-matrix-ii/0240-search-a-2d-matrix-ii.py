class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            left, right = 0, len(row) - 1

            while left <= right:
                mid = (left + right) // 2
                look = row[mid]

                if look == target: return True
                elif look < target: left = mid + 1
                else: right = mid - 1

        return False