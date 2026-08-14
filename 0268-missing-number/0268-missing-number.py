class Solution(object):
    def missingNumber(self, nums):
        min_num, max_num = min(nums), max(nums)
        for num in range(0, max_num):
            if num not in nums: return num

        return max_num + 1