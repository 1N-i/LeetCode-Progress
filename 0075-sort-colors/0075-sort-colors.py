class Solution(object):
    def sortColors(self, nums):
        left, right = 0, len(nums) - 1
        curr = 0

        while curr <= right:
            if nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                left += 1
                curr += 1
            elif nums[curr] == 1: curr += 1
            else:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1