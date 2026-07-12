class Solution(object):
    def finalString(self, s):
        ans = ""
        for letter in s:
            if letter == "i": ans = ans[::-1]
            else: ans += letter

        return ans