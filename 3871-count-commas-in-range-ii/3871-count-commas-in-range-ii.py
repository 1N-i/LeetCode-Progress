class Solution(object):
    def countCommas(self, n):
        if len(str(n)) <= 3: return 0
    
        ans = 0
        mult = 1000
        while mult <= n:
            ans += (n - mult + 1)
            mult *= 1000

        return ans