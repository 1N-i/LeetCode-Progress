class Solution(object):
    def findTheDifference(self, s, t):
        s = "".join(sorted(s))
        t = "".join(sorted(t))

        for p in range(len(t)):
            if p == len(s): return t[p]
            if s[p] != t[p]: return t[p]