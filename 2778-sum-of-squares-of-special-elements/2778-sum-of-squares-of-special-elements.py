class Solution(object):
    def sumOfSquares(self, nums):
        n = len(nums)
        ans = nums[0] * nums[0]

        for i in range(2, n + 1):
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]

        return ans