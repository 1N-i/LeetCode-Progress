class Solution(object):
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            maxNum = max(nums[:i + 1])
            minNum = min(nums[i:])

            if maxNum - minNum <= k: return i

        return -1