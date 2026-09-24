class Solution(object):
    def findDisappearedNumbers(self, nums):
        ranger = len(nums) + 1
        nums = set(nums)
        ans = set()
        
        for num in range(1, ranger):
            if num not in nums:
                ans.add(num)

        return list(ans)