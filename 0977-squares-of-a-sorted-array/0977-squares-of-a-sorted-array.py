class Solution(object):
    def sortedSquares(self, nums):
        new_list = [num ** 2 for num in nums]
        new_list.sort()
        return new_list