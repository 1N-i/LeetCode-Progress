class Solution(object):
    def findMiddleIndex(self, nums):
        sumT, sumL = sum(nums), 0
        for i in range(len(nums)):
            sumR = sumT - sumL - nums[i]
            
            if sumL == sumR: return i
            else: sumL += nums[i]

        return -1