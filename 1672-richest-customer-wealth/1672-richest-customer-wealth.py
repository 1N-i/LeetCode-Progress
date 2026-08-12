class Solution(object):
    def maximumWealth(self, accounts):
        richest = 0
        for i in accounts:
            richest = max(richest, sum(i))
        return richest
        