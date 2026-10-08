class Solution(object):
    def topKFrequent(self, words, k):
        guide = {}
        for word in words:
            guide[word] = guide.get(word, 0) + 1

        return sorted(guide.keys(), key=lambda w: (-guide[w], w))[:k]