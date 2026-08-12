class Solution(object):
    def maximumWealth(self, accounts):
        richest = 0
        for account in accounts:
            richest = max(richest, sum(account))
        return richest
        