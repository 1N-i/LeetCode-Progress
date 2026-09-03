class Solution(object):
    def minimumDeletions(self, nums):
        lenNums = len(nums)
        
        iMinN, iMaxN = nums.index(min(nums)), nums.index(max(nums))
        leftIndex, rightIndex = min(iMinN, iMaxN), max(iMinN, iMaxN)

        bothLeft = rightIndex + 1
        bothRight = lenNums - leftIndex
        oneEach = (leftIndex + 1) + (lenNums - rightIndex)
        
        return min(bothLeft, bothRight, oneEach)