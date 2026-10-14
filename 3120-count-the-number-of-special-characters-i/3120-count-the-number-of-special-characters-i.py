import string
class Solution(object):
    def numberOfSpecialChars(self, word):
        ans = 0
        lower = string.ascii_lowercase

        for l in lower:
            if l in word and l.upper() in word:
                ans += 1

        return ans