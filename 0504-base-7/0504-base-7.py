class Solution(object):
    def convertToBase7(self, num):
        if num == 0 or num == 1: return str(num)

        negative = False
        if num < 0:
            num *= -1
            negative = True

        ans = ""
        while num != 0:
            remain = num % 7
            ans += str(remain)
            num //= 7

        if negative == True: ans += "-"
        return ans[::-1]