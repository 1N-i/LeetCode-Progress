class Solution(object):
    def numIdenticalPairs(self, nums):
        ans, len_nums = 0, len(nums)
        for i in range(len_nums):
            num1 = nums[i]
            for j in range(i + 1, len_nums):
                if num1 == nums[j]: ans += 1

        return ans