class Solution(object):
    def hammingWeight(self, n):
        bin_n = bin(n)[2:]

        ans = 0
        for num in bin_n:
            ans += int(num)

        return ans