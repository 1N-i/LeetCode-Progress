class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0: return 1

        convertedNum = ""
        while n != 0:
            convertedNum += str(n % 2)
            n //= 2

        ans = ""
        for num in reversed(convertedNum):
            if num == "0": ans += "1"
            else: ans += "0"

        convertedAns = 0 
        ans = ans[::-1]
        for i in range(len(ans)):
            convertedAns += int(ans[i]) * (2 ** i)

        return convertedAns