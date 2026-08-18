class Solution(object):
    def missingNumber(self, nums):
        if 0 not in nums: return 0

        supposed_sum = sum(range(min(nums), max(nums) + 1))
        actual_sum = sum(nums)
        if supposed_sum == actual_sum:
            return max(nums) + 1 
        
        return supposed_sum - actual_sum