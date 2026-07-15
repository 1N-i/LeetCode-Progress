class Solution(object):
    def isHappy(self, n):
        seen = []
        while True:
            new_num = list(str(n))
            n = sum([(int(item) ** 2) for item in new_num])

            if n == 1: return True
            elif n in seen: return False
            seen.append(n)