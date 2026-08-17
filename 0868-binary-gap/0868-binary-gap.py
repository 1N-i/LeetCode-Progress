class Solution(object):
    def binaryGap(self, n):
        bin_n = bin(n)[2:]
        ans, temp = 0, 0

        left, right = 0, 0
        while right <= len(bin_n) - 1:
            if bin_n[left] == "1" and bin_n[right] == "1":
                ans = max(ans, temp)
                left = right
                temp = 0

            right += 1
            temp += 1

        return ans