class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans = []

        for num in nums:
            smaller = 0
            for n in nums:
                if num > n: smaller += 1

            ans.append(smaller)

        return ans