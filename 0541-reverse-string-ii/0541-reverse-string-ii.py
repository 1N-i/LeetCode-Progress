class Solution(object):
    def reverseStr(self, s, k):
        if len(s) <= k: return s[::-1]

        ans, temp_ans = "", ""
        first_k_reversed = False
        n_vezes = 0

        for i in range(len(s)):
            temp_ans += s[i]
            if first_k_reversed == False:
                if i == (k - 1) + (n_vezes * k * 2):
                    temp_ans = temp_ans[::-1]
                if i == (k - 1) * 2 + (n_vezes * k * 2):
                    first_k_reversed = True

            else:
                ans += temp_ans
                temp_ans = ""
                n_vezes += 1
                first_k_reversed = False

        if len(temp_ans) < k: temp_ans = temp_ans[::-1]

        return ans + temp_ans