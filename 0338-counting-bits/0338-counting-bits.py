class Solution(object):
    def countBits(self, num):
        ans = [0] * (num+1)
        for i in range(1, num+1):
            ans[i] = (ans[i >> 1] + i % 2)

        return ans