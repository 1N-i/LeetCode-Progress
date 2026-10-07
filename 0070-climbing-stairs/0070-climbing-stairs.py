class Solution(object):
    def climbStairs(self, n):
        prev, curr = 0, 1

        for _ in range(n):
            prev, curr = curr, prev + curr

        return curr