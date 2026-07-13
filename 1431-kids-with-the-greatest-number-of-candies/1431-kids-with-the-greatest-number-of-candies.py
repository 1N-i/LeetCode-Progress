class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans, maxCandy = [], max(candies)
        
        for candie in candies:
            if candie + extraCandies >= maxCandy:
                ans.append(True)

            else: ans.append(False)

        return ans