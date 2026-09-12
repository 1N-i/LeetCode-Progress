class Solution(object):
    def reverse(self, x):
        plus_minus = 1 if x > 0 else -1

        str_x = str(x * plus_minus)
        ans = "".join(num for num in reversed(str_x))

        int_ans = int(ans)

        if (-2)**31 < int_ans < 2**31 - 1: return int_ans * plus_minus
        return 0