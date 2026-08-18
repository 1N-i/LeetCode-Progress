class Solution(object):
    def missingNumber(self, nums):
        if 0 not in nums: return 0

        supposed_list = range(min(nums), max(nums) + 1)
        if sum(supposed_list) == sum(nums):
            return max(nums) + 1 
        
        return sum(supposed_list) - sum(nums)