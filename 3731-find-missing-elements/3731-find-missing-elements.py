class Solution(object):
    def findMissingElements(self, nums):
        min_value, max_value = min(nums), max(nums)
        ans = []

        for num in range(min_value, max_value):
            if num not in nums: ans.append(num)

        return ans