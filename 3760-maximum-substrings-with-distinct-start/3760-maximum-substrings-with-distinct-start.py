class Solution(object):
    def maxDistinct(self, s):
        guide = {}

        for l in s:
            guide[l] = guide.get(l, 0) + 1

        return len(guide)