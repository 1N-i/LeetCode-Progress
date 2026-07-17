class Solution(object):
    def commonFactors(self, a, b):
        ans = 0
        
        for fact in range(1, max(a, b) + 1):
            if a % fact == 0 and b % fact == 0:
                ans += 1

        return ans