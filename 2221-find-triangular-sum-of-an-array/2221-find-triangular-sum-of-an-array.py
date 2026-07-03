class Solution(object):
    def triangularSum(self, nums):
        while len(nums) != 1:
            for i in range(len(nums) - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            nums.pop()

        return nums[0]