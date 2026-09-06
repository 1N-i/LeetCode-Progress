class Solution(object):
    def transformArray(self, nums):
        ans = []

        for num in nums:
            if num % 2 == 0: ans.append(0)
            else: ans.append(1)

        return sorted(ans)