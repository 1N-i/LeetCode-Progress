class Solution(object):
    def firstMissingPositive(self, nums):
        sup = 1
        nums = list(set(nums))
        for num in sorted(nums):
            if num <= 0: continue

            if num == sup:
                sup += 1
            else:
                return sup

        return sup