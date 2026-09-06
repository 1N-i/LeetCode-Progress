class Solution(object):
    def pivotIndex(self, nums):
        sumT = sum(nums)
        sumL = 0
        for i in range(len(nums)):
            sumR = sumT - sumL - nums[i]
            if sumL == sumR: return i
            else: sumL += nums[i]

        return -1