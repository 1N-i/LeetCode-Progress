class Solution(object):
    def reverse(self, x):
        x_copy = x
        if x < 0: x_copy *= -1

        str_x = str(x_copy)
        ans = ""

        for num in str_x[::-1]:
            ans += num

        if int(ans) > 2**31 - 1: return 0

        if x > 0: return int(ans)
        else: return int(ans) * -1