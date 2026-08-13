class Solution(object):
    def majorityElement(self, nums):
        ans = {}

        for num in nums:
            if num not in ans: ans[num] = 1
            else: ans[num] += 1

        return max(ans, key=ans.get)