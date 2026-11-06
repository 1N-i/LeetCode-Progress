class Solution(object):
    def isAnagram(self, s, t):
        guide_s, guide_t = {}, {}

        for l in s:
            guide_s[l] = guide_s.get(l, 0) + 1

        for l in t:
            guide_t[l] = guide_t.get(l, 0) + 1

        return guide_s == guide_t