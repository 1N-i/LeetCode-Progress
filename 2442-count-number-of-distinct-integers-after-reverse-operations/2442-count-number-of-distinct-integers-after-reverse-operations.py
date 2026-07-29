class Solution(object):
    def countDistinctIntegers(self, nums):
        ans = set(nums)
        for num in nums:
            ans.add(int(str(num)[::-1]))

        return len(ans)