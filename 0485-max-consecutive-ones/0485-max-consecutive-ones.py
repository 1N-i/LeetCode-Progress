class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_one = 0
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
            else:
                if max_one < ones:
                    max_one = ones
                ones = 0
        if max_one < ones:
            max_one = ones

        return max_one