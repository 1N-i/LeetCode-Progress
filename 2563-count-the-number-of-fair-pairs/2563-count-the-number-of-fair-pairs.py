class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        ans = 0
        left, right = 0, len(nums) - 1

        for _ in range(len(nums)):
            if nums[left] + nums[right] <= upper:
                ans += (right - left)
                left += 1
            else:
                right -= 1
        
        left, right = 0, len(nums) - 1
        for _ in range(len(nums)):
            if nums[left] + nums[right] < lower:
                ans -= (right - left)
                left += 1
            else:
                right -= 1
        
        return ans