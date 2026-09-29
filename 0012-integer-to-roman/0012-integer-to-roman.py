class Solution:
    def intToRoman(self, num):
        guide = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"]
        ]

        ans = ""
        for i in range(13):
            while num >= guide[i][0]:
                ans += guide[i][1]
                num -= guide[i][0]

        return ans