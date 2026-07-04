class Solution(object):
    def findWordsContaining(self, words, x):
        result = []
        for i in range(len(words)):
            if x in list(words[i]): result.append(i)

        return list(set(result))