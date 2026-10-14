class Solution(object):
    def numberOfSpecialChars(self, word):
        ans = 0
        guide = {}

        for i, l in enumerate(word):
            if l.isupper():
                if l not in guide:
                    guide[l] = i
            else:
                guide[l] = i

        for l in guide:
            if l.isupper() and l.lower() in guide:
                if guide[l] > guide[l.lower()]:
                    ans += 1

        return ans