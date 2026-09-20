class Solution(object):
    def reverseDegree(self, s):
        guide = {
            'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, 'g': 6, 'f': 5, 'i': 8, 'h': 7, 'k': 10, 'j': 9, 'm': 12, 'l': 11, 'o': 14, 'n': 13, 'q': 16, 'p': 15, 's': 18, 'r': 17, 'u': 20, 't': 19, 'w': 22, 'v': 21, 'y': 24, 'x': 23, 'z': 25
        }

        ans = 0
        for i, l in enumerate(s):
            ans += (26 - guide[l]) * (i + 1)

        return ans