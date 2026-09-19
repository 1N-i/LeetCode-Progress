class Solution(object):
    def numIdenticalPairs(self, nums):
        ans = 0
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i + 1, len(nums)):
                if num1 == nums[j]: ans += 1

        return ans