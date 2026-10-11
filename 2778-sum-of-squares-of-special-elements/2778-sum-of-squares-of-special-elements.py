class Solution(object):
    def sumOfSquares(self, nums):
        n = len(nums)
        ans = []

        for i in range(1, n + 1):
            if n % i == 0:
                ans.append(nums[i - 1] ** 2)

        return sum(ans)