class Solution(object):
    def mySqrt(self, x):
        i = 0
        while i <= x + 1:
            if i ** 2 == x:
                return i
            elif i ** 2 > x:
                return i - 1
            i += 1