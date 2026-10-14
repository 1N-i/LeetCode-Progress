import string
class Solution(object):
    def numberOfSpecialChars(self, word):
        ans = 0
        for l in string.ascii_lowercase:
            if l in word and l.upper() in word:
                ans += 1

        return ans