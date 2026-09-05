class Solution:
    def maxProfit(self, prices):
        profit, buy = 0, prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy: buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
                
        return profit