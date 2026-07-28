class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        seen_sign = False
        ans = ""

        for char in s:
            if seen_sign == False:
                if char == "-" or char == "+":
                    ans += char
                    seen_sign = True
                    continue

            if not char.isdigit(): break

            ans += char
            seen_sign = True

        if ans == "" or ans == "-" or ans == "+": return 0

        if int(ans) < (-2)**31: return (-2)**31
        if int(ans) > 2**31 - 1: return 2**31 - 1
         
        return int(ans)