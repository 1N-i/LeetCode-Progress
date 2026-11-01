class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]

        ans = 0
        for num in nums:
            ans += abs(num - median)
        return ans