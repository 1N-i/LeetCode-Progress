class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        def countUntilLimit(limit):
            ans = 0
            left, right = 0, len(nums) - 1
            for _ in range(len(nums)):
                if nums[left] + nums[right] <= limit:
                    ans += (right - left)
                    left += 1
                else:
                    right -= 1

            return ans

        nums.sort()
        return countUntilLimit(upper) - countUntilLimit(lower - 1)