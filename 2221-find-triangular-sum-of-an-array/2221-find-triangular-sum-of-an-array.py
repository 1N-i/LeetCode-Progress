class Solution(object):
    def triangularSum(self, nums):
        n = len(nums)
        coeff = 1
        ans = 0

        for i in range(n):
            ans += nums[i] * coeff
            coeff = coeff * (n - 1 - i) // (i + 1)

        return ans % 10