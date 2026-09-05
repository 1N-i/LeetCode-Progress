class Solution:
    def maxProfit(self, prices):
        profit, buy = 0, prices[0]

        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > profit:
                profit = price - buy

        return profit