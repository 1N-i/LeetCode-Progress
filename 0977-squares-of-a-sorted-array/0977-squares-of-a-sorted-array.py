class Solution(object):
    def sortedSquares(self, nums):
        return sorted([num ** 2 for num in nums])