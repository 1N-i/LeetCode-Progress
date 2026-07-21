class Solution(object):
    def reverseBits(self, n):
        bin_n = bin(n)[2:].zfill(32)
        ans = bin_n[::-1]

        return int(ans, 2)