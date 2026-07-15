class Solution(object):
    def isHappy(self, n):
        seen = set()
        while True:
            seen.add(n)
            total = 0
            for num in str(n):
                total += int(num) ** 2
            n = total

            if n == 1: return True
            elif n in seen: return False