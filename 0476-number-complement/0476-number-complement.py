class Solution(object):
    def findComplement(self, n):
        if n == 0: return 1

        convertedNum = ""
        while n != 0:
            convertedNum += str(n % 2)
            n //= 2

        ans = ""
        for num in reversed(convertedNum):
            if num == "0": ans += "1"
            else: ans += "0"

        return int(ans, 2)