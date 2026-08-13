class Solution(object):
    def majorityElement(self, nums):
        ans = {}

        for num in nums:
            str_num = str(num)
            if str_num not in ans: ans[str_num] = 1
            else: ans[str_num] += 1

        return int(max(ans, key=ans.get))