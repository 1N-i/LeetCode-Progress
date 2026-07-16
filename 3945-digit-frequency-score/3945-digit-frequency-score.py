class Solution(object):
    def digitFrequencyScore(self, n):
        list_n = list(str(n))

        return sum(int(num) for num in list_n)