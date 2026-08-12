class Solution(object):
    def maximumWealth(self, accounts):
        richest = 0
        for account in accounts:
            if sum(account) > richest:
                richest = sum(account)

        return richest