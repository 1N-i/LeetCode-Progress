class Solution(object):
    def mapWordWeights(self, words, weights):
        ans = []
        for s in words:
            count = 0
            for i in range(len(s)):
                count += weights[ord(s[i]) - ord('a')]
            ans.append(chr(ord('a') + (25 - (count % 26))))
            
        return "".join(ans)