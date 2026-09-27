class Solution(object):
    def twoSum(self, nums, target):
        guide = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in guide:
                return [guide[comp] + 1, i + 1]

            guide[num] = i