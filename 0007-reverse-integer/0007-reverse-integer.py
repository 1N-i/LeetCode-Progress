class Solution(object):
    def reverse(self, x):
        plus_minus = 1 if x > 0 else -1

        ans = int(str(x * plus_minus)[::-1])

        if (-2)**31 < ans < 2**31 - 1: return ans * plus_minus
        return 0