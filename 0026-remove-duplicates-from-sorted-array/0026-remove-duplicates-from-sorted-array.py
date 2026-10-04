class Solution(object):
    def removeDuplicates(self, nums):
        seen = []
        underline = 0
        for num in nums:
            if num in seen:
                underline += 1
            else:
                seen.append(num)
        
        nums[:] = sorted(seen) + ["_"] * underline
        return len(seen)