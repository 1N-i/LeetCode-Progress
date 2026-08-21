class Solution(object):
    def diStringMatch(self, s):
        perm = [0] * (len(s) + 1)
        low, high = 0, len(s)
        i = 0

        while i <= len(s) - 1:
            if s[i] == "I":
                perm[i] = low
                low += 1

            else: #s[i] == "D"
                perm[i] = high
                high -= 1

            i += 1

        perm[i] = high
        return perm