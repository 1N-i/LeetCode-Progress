class Solution(object):
    def canAliceWin(self, n):
        if n < 10: return False

        for removal in range(10, 0, -1):
            n -= removal
            if n < 0:
                return removal % 2 != 0