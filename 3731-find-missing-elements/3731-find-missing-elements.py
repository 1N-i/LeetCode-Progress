class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        ans = []
        for num in range(nums[0], nums[-1]):
            if num not in nums: ans.append(num)

        return ans