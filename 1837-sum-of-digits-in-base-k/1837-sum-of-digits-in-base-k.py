class Solution(object):
    def sumBase(self, n, k):
        convertedNum = ""
        while n != 0:
            convertedNum += str(n % k)
            n //= k

        ans = 0
        for num in reversed(convertedNum):
            ans += int(num)

        return ans