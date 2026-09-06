class Solution(object):
    def minimumRecolors(self, blocks, k):
        left, right = 0, 0
        minS, temp = len(blocks), 0

        while left <= len(blocks) - k:
            if blocks[right] == "W":
                temp += 1

            right += 1
            if right == left + k:
                minS = min(minS, temp)
                temp = 0
                left += 1
                right = left

        return minS