import string
class Solution(object):
    def numberOfSpecialChars(self, word):
        ans = 0
        upper = string.ascii_uppercase

        for l in set(word):
            if l in upper and l.lower() in word:
                ans += 1

        return ans