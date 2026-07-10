class Solution(object):
    def searchInsert(self, nums, target):
        if nums[-1] < target: return len(nums)
        if nums[0] > target: return 0

        for num in nums:
            if num >= target:
                return nums.index(num)