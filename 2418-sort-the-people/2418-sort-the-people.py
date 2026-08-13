class Solution(object):
    def sortPeople(self, names, heights):
        sorted_height = sorted(heights, reverse=True)
        ans = []

        for i in sorted_height:
            ans.append(names[heights.index(i)])

        return ans