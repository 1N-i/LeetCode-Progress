class Solution(object):
    def firstUniqChar(self, s):
        guide = {}
        for l in s:
            guide[l] = guide.get(l, 0) + 1

        for l in s:
            if guide[l] == 1:
                return s.index(l)

        return -1