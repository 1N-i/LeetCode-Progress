class Solution(object):
    def commonFactors(self, a, b):
        maxAB = max(a, b)
        ans = 0
        
        for fact in range(1, maxAB + 1):
            if a % fact == 0 and b % fact == 0:
                ans += 1

        return ans