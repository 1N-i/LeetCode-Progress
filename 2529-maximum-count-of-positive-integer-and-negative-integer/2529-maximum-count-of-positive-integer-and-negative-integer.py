class Solution(object):
    def maximumCount(self, nums):
        pos, neg, zeros = 0, 0, 0
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0: left = mid + 1
            else: right = mid - 1

        neg = left
        left, right = mid, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= 0: left = mid + 1
            else: right = mid - 1

        pos = len(nums) - left
        return max(neg, pos)