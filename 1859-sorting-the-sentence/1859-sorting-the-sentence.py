class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        result = [""] * len(words)

        for word in words:
            i = int(word[-1]) - 1
            result[i] = word[:-1]

        ans = " ".join(result)
        return ans