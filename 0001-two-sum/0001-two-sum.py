class Solution(object):
    def twoSum(self, nums, target):
        left = 0

        while left < len(nums):
            right = left + 1
            while right < len(nums):
                if nums[left] + nums[right] == target:
                    return [left, right]
                right += 1

            left += 1