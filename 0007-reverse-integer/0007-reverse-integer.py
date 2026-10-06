class Solution(object):
    def reverse(self, x):
        if x > 0: plus_minus = 1
        else:
            plus_minus = -1
            x *= -1

        str_x = str(x)
        ans = ""
        for num in str_x[::-1]:
            ans += num

        if (-2)**31 < int(ans) < 2**31 - 1: return int(ans) * plus_minus
        return 0