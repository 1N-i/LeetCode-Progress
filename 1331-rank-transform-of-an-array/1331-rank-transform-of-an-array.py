class Solution(object):
    def arrayRankTransform(self, arr):
        rank = 1
        ranking = {}

        for num in sorted(arr):
            if num not in ranking:
                ranking[num] = rank
                rank += 1

        for i in range(len(arr)):
            arr[i] = ranking[arr[i]]

        return arr