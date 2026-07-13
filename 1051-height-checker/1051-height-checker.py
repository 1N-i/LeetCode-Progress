class Solution(object):
    def heightChecker(self, heights):
        sorted_height = sorted(heights)
        same = 0

        for i in range(len(heights)):
            if sorted_height[i] != heights[i]:
                same += 1

        return same