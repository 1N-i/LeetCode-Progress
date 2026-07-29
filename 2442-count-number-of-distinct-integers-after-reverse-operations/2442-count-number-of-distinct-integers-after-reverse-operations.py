class Solution(object):
    def countDistinctIntegers(self, nums):
        ans = set(nums)
        for num in nums:
            ans.add(self.reverseNum(str(num)))

        return len(ans)

    def reverseNum(self, str_num):
        return int(str_num[::-1])