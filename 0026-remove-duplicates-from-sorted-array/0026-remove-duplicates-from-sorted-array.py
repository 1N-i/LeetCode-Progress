class Solution(object):
    def removeDuplicates(self, nums):
        seen = set()
        underline, size_max = 0, len(nums)
        for num in nums:
            if num in seen:
                underline += 1
            else:
                seen.add(num)
        
        nums[:] = sorted(list(seen)) + ["_"] * underline
        return len(seen)