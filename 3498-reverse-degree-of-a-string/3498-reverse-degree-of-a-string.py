import string
class Solution(object):
    def reverseDegree(self, s):
        alphabet = string.ascii_lowercase

        ans = 0
        for i, l in enumerate(s):
            ans += (26 - alphabet.index(l)) * (i + 1)

        return ans