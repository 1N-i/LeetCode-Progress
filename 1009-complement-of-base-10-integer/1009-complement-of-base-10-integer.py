class Solution(object):
    def bitwiseComplement(self, n):
        convertedNum = bin(n)

        ans = ""
        for num in convertedNum[2:]:
            if num == "0": ans += "1"
            else: ans += "0"

        return int(ans, 2)