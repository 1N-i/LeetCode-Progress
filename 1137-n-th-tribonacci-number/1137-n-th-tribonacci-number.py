class Solution(object):
    def tribonacci(self, n):
        if n == 0: return 0
        if n <= 2: return 1
        
        guide = [0] * (n + 1)
        guide[1], guide[2] = 1, 1

        for i in range(3, n + 1):
            guide[i] = guide[i-1] + guide[i-2] + guide[i-3]

        return guide[-1]