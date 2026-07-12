class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_array = sorted(arr)
        rank = 1
        ranking = {}

        for num in sorted_array:
            if num not in ranking:
                ranking[num] = rank
                rank += 1

        for i in range(len(arr)):
            arr[i] = ranking[arr[i]]

        return arr