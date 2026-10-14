class Solution(object):
    def numberOfSpecialChars(self, word):
        ans = 0
        guide = {}

        for i, l in enumerate(word):
            if l.isupper():
                guide.setdefault(l, i)
            else:
                guide[l] = i

        for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if l in guide and l.lower() in guide and guide[l] > guide[l.lower()]:
                ans += 1

        return ans