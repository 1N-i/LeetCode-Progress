class Solution(object):
    def reverseVowels(self, s):
        v = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        left, right = 0, len(s) - 1
        s_list = list(s)

        while left <= right:
            if s[left] in v and s[right] in v:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            elif s[left] in v: right -= 1
            elif s[right] in v: left += 1
            else:
                right -= 1
                left += 1

        return "".join(s_list)