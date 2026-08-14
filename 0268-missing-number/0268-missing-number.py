class Solution(object):
    def missingNumber(self, nums):
        max_num = max(nums)
        for num in range(0, max_num):
            if num not in nums: return num

        return max_num + 1