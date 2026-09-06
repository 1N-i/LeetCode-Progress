class Solution(object):
    def minimumRecolors(self, blocks, k):
        temp = 0
        for i in range(k):
            if blocks[i] == "W": temp += 1

        minS = min(k, temp)
        for right in range(k, len(blocks)):
            if blocks[right - k] == "W": temp -= 1 #Left pointer
            if blocks[right] == "W": temp += 1
            minS = min(minS, temp)

        return minS