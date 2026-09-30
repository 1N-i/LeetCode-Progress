class Solution(object):
    def reverseWords(self, s):
        ans = s.split()
        return " ".join(reversed(ans))