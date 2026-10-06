class Solution(object):
    def reverse(self, x):
        if x > 0: plus_minus = 1
        else: plus_minus = -1

        x = abs(x)
        ans = int(str(x)[::-1])

        if (-2)**31 < ans < 2**31 - 1: return ans * plus_minus
        return 0