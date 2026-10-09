class Solution(object):
    def countUntilLimit(self, nums, limit):
        ans = 0
        left, right = 0, len(nums) - 1
        for _ in range(len(nums)):
            if nums[left] + nums[right] <= limit:
                ans += (right - left)
                left += 1
            else:
                right -= 1

        return ans

    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        
        return self.countUntilLimit(nums, upper) - self.countUntilLimit(nums, lower - 1)