class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        max_num = nums[-1]
        for num in range(0, max_num):
            if num != nums[num]: return num

        return max_num + 1