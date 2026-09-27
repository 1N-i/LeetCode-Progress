class Solution(object):
    def twoSum(self, nums, target):
        history = {}
        for i, num in enumerate(nums):
            objective = target - num
            if objective in history:
                return sorted([history[objective] + 1, i + 1])
            history[num] = i