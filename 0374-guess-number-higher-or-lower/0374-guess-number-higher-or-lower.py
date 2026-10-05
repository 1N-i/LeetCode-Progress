class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            pick = guess(mid)

            if pick == 0: return mid
            if pick == 1:
                left = mid + 1
            else:
                right = mid - 1