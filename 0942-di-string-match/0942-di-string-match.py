class Solution(object):
    def diStringMatch(self, s):
        perm = []
        low, high = 0, len(s)

        for l in s:
            if l == "I":
                perm.append(low)
                low += 1

            else: #l == "D"
                perm.append(high)
                high -= 1

        perm.append(high)
        return perm