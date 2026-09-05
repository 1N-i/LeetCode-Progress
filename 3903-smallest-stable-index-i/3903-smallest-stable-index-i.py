class Solution(object):
    def firstStableIndex(self, nums, k):
        maxNum, prefixMax = nums[0], []
        for num in nums:
            if num > maxNum:
                maxNum = num
            prefixMax.append(maxNum)

        minNum, sufixMin = nums[-1], []
        for num in reversed(nums):
            if num < minNum:
                minNum = num
            sufixMin.append(minNum)

        sufixMin = sufixMin[::-1]

        for i in range(len(nums)):
            if prefixMax[i] - sufixMin[i] <= k:
                return i

        return -1