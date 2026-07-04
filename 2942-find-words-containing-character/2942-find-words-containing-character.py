class Solution(object):
    def findWordsContaining(self, words, x):
        result = []
        for i in range(len(words)):
            for l in words[i]:
                if l in x: result.append(i)

        return list(set(result))