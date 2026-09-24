class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums_set = set(nums)
        ans = set()
        
        for num in range(1, len(nums) + 1):
            if num not in nums_set:
                ans.add(num)

        return list(ans)