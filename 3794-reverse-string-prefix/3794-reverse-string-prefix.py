class Solution:
    def reversePrefix(self, s, k):
        s = list(s)
        i = 0
        k -= 1

        while i < k:
            s[i], s[k] = s[k], s[i]
            i += 1
            k -= 1

        return "".join(s)