class Solution(object):
    def longestConsecutive(self, nums):
        if not nums: return 0

        setNums = sorted(set(nums))
        max_streak = 1
        current_streak = 1

        for i in range(1, len(setNums)):
            if setNums[i] == setNums[i-1] + 1:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 1
        return max(max_streak, current_streak)