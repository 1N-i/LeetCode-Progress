class Solution(object):
    def findDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else: return num