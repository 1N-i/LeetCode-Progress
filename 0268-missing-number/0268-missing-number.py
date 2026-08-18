class Solution(object):
    def missingNumber(self, nums):
        if 0 not in nums: return 0

        if sum(range(min(nums), max(nums) + 1)) == sum(nums):
            return max(nums) + 1 
        
        return sum(range(min(nums), max(nums) + 1)) - sum(nums)