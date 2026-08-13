class Solution(object):
    def isPalindrome(self, x):
        xStr = str(x)
        if "-" in xStr:
            return False
        
        xReverse = xStr[::-1]
        return xReverse == xStr