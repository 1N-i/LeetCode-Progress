class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            try_num = guess(mid)

            if try_num == 1:
                left = mid + 1
            elif try_num == -1:
                right = mid - 1
            else:
                return mid           