class Solution(object):
    def fib(self, n):
        if n < 2: return n

        list_f = [0, 1]

        before, last = 0, 1

        for i in range(n - 1):
            list_f.append(before + last)
            before, last = last, before + last

        return list_f[-1]     