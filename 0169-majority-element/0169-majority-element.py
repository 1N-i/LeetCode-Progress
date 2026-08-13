class Solution(object):
    def majorityElement(self, nums):
        ans = {}

        for num in nums:
            ans[num] = ans.get(num, 0) + 1

        return max(ans, key=ans.get)