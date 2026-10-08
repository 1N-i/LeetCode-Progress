class Solution(object):
    def firstMissingPositive(self, nums):
        sup = 1
        seen = set()
        nums.sort()
        for num in nums:
            if (num <= 0) or (num in seen): continue
            seen.add(num)

            if num == sup:
                sup += 1
            else:
                return sup

        return sup