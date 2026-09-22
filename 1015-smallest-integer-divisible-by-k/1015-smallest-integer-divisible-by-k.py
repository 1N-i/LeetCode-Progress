class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k % 10 not in {1, 3, 7, 9}: return -1

        n = 1
        for _ in range(1, k + 1):
            if n % k == 0: return len(str(n))

            n *= 10
            n += 1

        return -1