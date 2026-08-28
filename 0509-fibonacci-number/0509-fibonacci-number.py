class Solution(object):
    def fib(self, n):
        if n < 2: return n
        before, last = 1, 1

        for _ in range(1, n - 1):
            before, last = last, before + last

        return last