class Solution(object):
    def sumBase(self, n, k):
        import string

        convertedNum = ""
        chars = string.digits + string.ascii_uppercase
        while n != 0:
            remain = n % k
            convertedNum += chars[remain]
            n //= k

        ans = 0
        for num in reversed(convertedNum):
            ans += int(num)

        return ans