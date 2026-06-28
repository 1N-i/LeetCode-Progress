class Solution(object):
    def maxProfit(self, prices):
        day_to_buy, day_to_sell = 0, 1
        maxP = 0

        while day_to_sell < len(prices):
            if prices[day_to_buy] < prices[day_to_sell]:
                maxP = max(maxP, prices[day_to_sell] - prices[day_to_buy])
            else:
                day_to_buy = day_to_sell
            day_to_sell += 1

        return maxP