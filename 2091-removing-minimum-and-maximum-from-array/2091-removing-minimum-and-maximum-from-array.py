class Solution(object):
    def minimumDeletions(self, nums):
        lenNums = len(nums)
        if lenNums <= 2: return lenNums

        iMinN, iMaxN = nums.index(min(nums)), nums.index(max(nums))
        leftIndex, rightIndex = min(iMinN, iMaxN), max(iMinN, iMaxN)
        
        return min(len(nums[:rightIndex]) + 1, len(nums[leftIndex:]), len(nums[:leftIndex]) + 1 + len(nums[rightIndex:]))