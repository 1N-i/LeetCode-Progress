class Solution(object):
    def isPalindrome(self, x):
        xList = list(str(x))
        if "-" in xList:
            return False
        
        xReverse = xList[:]
        xReverse.reverse()
        return xReverse == xList