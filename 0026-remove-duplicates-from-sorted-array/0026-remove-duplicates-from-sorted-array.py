class Solution(object):
    def removeDuplicates(self, nums):
        seen = set()
        underline = 0
        for num in nums:
            if num in seen:
                underline += 1
            seen.add(num)
        
        nums[:] = sorted(list(seen))
        return len(seen)