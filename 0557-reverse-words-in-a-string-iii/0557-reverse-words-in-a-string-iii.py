class Solution(object):
    def reverseWords(self, s):
        split_s = s.split()
        ans = ""

        for i in range(len(split_s)):
            if i == 0: ans += split_s[i][::-1]
            else: ans += " " + split_s[i][::-1]

        return ans