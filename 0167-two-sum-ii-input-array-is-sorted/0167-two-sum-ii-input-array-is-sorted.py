class Solution(object):
    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            ans = nums[left] + nums[right]
            if ans < target:
                left += 1
            elif ans > target:
                right -= 1
            else:
                return [left + 1, right + 1]