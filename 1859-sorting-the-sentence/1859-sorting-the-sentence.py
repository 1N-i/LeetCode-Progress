class Solution(object):
    def sortSentence(self, s):
        guide = {}

        s_list = s.split()
        for word in s_list:
            guide[word[-1]] = word[:-1]

        ans = ""
        for num in range(1, len(s_list) + 1):
            ans += guide[str(num)]
            if num != len(s_list):
                ans += " "

        return ans