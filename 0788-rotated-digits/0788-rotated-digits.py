class Solution(object):
    def rotatedDigits(self, n):
        ans = 0

        for num in range(1, n + 1):
            str_num = str(num)
            if "3" in str_num or "4" in str_num or "7" in str_num: ans += 1
            else:
                new_num = ""
                for Num in str_num:
                    if Num == "2": new_num += "5"
                    elif Num == "5": new_num += "2"
                    elif Num == "6": new_num += "9"
                    elif Num == "9": new_num += "6"
                    else: new_num += Num #0, 1, 8

                if new_num == str_num: ans += 1

        return n - ans