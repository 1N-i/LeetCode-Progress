class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        w1, w2 = "", ""

        for l in word1:
            w1 += l

        for l in word2:
            w2 += l

        return w1 == w2