class Solution(object):
    def firstMissingPositive(self, nums):
        sup = 1
        nums.sort()
        for num in nums:
            if num == sup:
                sup += 1

        return sup