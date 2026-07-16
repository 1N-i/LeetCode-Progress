class Solution(object):
    def digitFrequencyScore(self, n):
        return sum(int(num) for num in list(str(n)))