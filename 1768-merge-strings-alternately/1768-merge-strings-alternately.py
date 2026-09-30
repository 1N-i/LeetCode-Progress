class Solution(object):
    def mergeAlternately(self, word1, word2):
        p1, p2 = 0, 0
        ans = ""

        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                ans += word1[p1]
                p1 += 1
            if p2 < len(word2):
                ans += word2[p2]
                p2 += 1

        return ans