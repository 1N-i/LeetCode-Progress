class Solution(object):
    def firstMissingPositive(self, nums):
        sup = 1
        seen = set()
        nums.sort()
        for num in nums:
            if num <= 0: continue
            if num not in seen:
                seen.add(num)
            else: continue
            
            if num == sup:
                sup += 1
            else:
                return sup

        return sup