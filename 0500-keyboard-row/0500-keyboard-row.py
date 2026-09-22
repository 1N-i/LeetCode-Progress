class Solution(object):
    def findWords(self, words):
        ans = []
        fir_row = set("qwertyuiop")
        sec_row = set("asdfghjkl")
        thi_row = set("zxcvbnm")
        for word in words:
            fr = 0
            sr = 0
            tr = 0
            lower_word = word.lower()
            for l in lower_word:
                if l in fir_row:
                    fr = 1
                if l in sec_row:
                    sr = 1
                if l in thi_row:
                    tr = 1

                if fr + sr + tr >= 2: break

            if fr + sr + tr == 1:
                ans.append(word)

        return ans