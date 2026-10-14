class Solution(object):
    def numberOfSpecialChars(self, word):
        ans = 0
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        guide = {}

        for i, l in enumerate(word):
            if l in upper and l not in guide:
                guide[l] = i
            elif l not in upper:
                guide[l] = i

        for l in guide:
            if l in upper and l.lower() in word and guide[l] > guide[l.lower()]:
                ans += 1

        return ans