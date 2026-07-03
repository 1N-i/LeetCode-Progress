class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if i == j: j += 1
                if nums[i] + nums[j] == target: return i, j