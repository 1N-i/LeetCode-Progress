class Solution(object):
    def findTheDifference(self, s, t):
        map1, map2 = {}, {}

        for l in s:
            map1[l] = map1.get(l, 0) + 1

        for l in t:
            map2[l] = map2.get(l, 0) + 1

        for l in map2:
            if l not in map1: return l
            if map2[l] > map1[l]: return l