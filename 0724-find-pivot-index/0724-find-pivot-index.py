class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            leftSum = sum(nums[:i + 1])
            rightSum = sum(nums[i:])

            if leftSum == rightSum: return i

        return -1