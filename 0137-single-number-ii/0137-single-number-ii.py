class Solution(object):
    def singleNumber(self, nums):
        supposed_sum = sum(set(nums)) * 3
        return (supposed_sum - sum(nums)) / 2