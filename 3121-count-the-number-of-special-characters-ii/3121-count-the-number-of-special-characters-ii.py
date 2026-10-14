class Solution(object):
    def numberOfSpecialChars(self, word):
        ans = 0
        guide = {}

        for i, l in enumerate(word):
            if l not in guide:
                guide[l] = []
            guide[l].append(i)

        for l in guide:
            if l.isupper() and l.lower() in word:
                if guide[l][0] > guide[l.lower()][-1]:
                    ans += 1

        return ans