class Solution(object):
    def getSum(self, a, b):
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            soma = (a ^ b) & MASK
            transporte = ((a & b) << 1) & MASK
            a, b = soma, transporte

        return a if a <= MAX_INT else ~(a ^ MASK)