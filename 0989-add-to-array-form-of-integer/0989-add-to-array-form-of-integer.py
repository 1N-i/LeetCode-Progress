class Solution(object):
    def addToArrayForm(self, num, k):
        actual_num = int("".join(map(str, num)))

        ans = list(str(actual_num + k))
        answ = [int(n) for n in ans]
        return answ