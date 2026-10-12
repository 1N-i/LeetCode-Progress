class Solution(object):
    def sortedSquares(self, nums):
        ans = [num * num for num in nums]
        ans.sort()
        
        return ans