class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if flowerbed == [0]: return True
        if n == 0 or (sum(flowerbed) == 0 and sum(flowerbed) >= n * 2): return True
        if len(flowerbed) == n: return False
        if flowerbed[0] == 0 and flowerbed[1] == 0 and n > 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0 and n > 0:
            flowerbed[-1] = 1
            n -= 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0 and n > 0:
                flowerbed[i] = 1
                n -= 1

        return n == 0