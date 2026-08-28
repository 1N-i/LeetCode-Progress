class Solution(object):
    def fib(self, n):
        if n < 2: return n
        before, last = 0, 1

        for _ in range(n - 1):
            before, last = last, before + last

        return last