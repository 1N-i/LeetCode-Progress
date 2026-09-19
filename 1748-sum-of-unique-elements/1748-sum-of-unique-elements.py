class Solution(object):
    def sumOfUnique(self, nums):
        guide = {}

        for num in nums:
            guide[num] = guide.get(num, 0) + 1

        ans = 0
        for num in guide:
            if guide[num] != 1: continue
            ans += num

        return ans