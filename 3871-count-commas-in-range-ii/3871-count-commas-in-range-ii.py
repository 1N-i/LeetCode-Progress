class Solution(object):
    def countCommas(self, n):
        if len(str(n)) <= 3: return 0
    
        ans = 0
        for exp in range(3, len(str(n)), 3):
            mult = 10 ** exp
            ans += (n - mult + 1)

        return ans