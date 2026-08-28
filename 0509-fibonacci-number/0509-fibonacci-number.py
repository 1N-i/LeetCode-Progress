class Solution(object):
    def fib(self, n):
        if n < 2: return n
        before, last = 0, 1

        for i in range(n - 1): #Just updates the variables
            before, last = last, before + last

        return last