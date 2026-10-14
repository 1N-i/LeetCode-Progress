class Solution(object):
    def numberOfSpecialChars(self, word):
        ans = 0
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        guide = {}

        for i, l in enumerate(word):
            guide.setdefault(l, []).append(i)

        for l in guide:
            if l in upper and l.lower() in word and guide[l][0] > guide[l.lower()][-1]:
                ans += 1

        return ans