class Solution(object):
    def isPowerOfThree(self, n):
        if n == 0: return False
        if n == 1: return True
        while n % 3 == 0:
            n /= 3
            if n == 1: return True

        return False