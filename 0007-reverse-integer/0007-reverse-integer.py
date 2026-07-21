class Solution(object):
    def reverse(self, x):
        if x > 0: plus_minus = 1
        else:
            plus_minus = -1
            x *= -1

        str_x = str(x)
        ans = str_x[::-1]

        int_ans = int(ans)

        if (-2)**31 < int_ans < 2**31 - 1: return int_ans * plus_minus
        return 0