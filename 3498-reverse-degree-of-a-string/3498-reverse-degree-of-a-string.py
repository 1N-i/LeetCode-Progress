import string
class Solution(object):
    def reverseDegree(self, s):
        alphabet = string.ascii_lowercase
        guide = {}
        for i, l in enumerate(alphabet):
            guide[l] = i

        ans = 0
        for i, l in enumerate(s):
            ans += (26 - guide[l]) * (i + 1)

        return ans