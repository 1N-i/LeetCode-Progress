class Solution(object):
    def mySqrt(self, x):
        if x == 0: return 0
        if x <= 3: return 1
        left, right = 2, x

        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid
            if squared == x: return mid
            elif squared < x: left = mid + 1
            else: right = mid - 1

        return right