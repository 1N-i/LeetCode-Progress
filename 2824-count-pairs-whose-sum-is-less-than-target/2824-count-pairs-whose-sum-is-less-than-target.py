class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            objective = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] < objective:
                    ans += 1
                else:
                    break

        return ans