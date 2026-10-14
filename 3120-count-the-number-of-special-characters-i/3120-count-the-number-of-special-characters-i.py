class Solution(object):
    def numberOfSpecialChars(self, word):
        ans = 0
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for l in set(word):
            if l in upper and l.lower() in word:
                ans += 1

        return ans