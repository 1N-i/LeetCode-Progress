class Solution(object):
    def reversePrefix(self, word, ch):
        prefix, other_letters, reverse_prefix = "", "", ""
        found_ch = False
        for letter in word:
            if found_ch: other_letters += letter
            else: prefix += letter

            if letter == ch: found_ch = True

        if found_ch == False: return prefix
        reverse_prefix = prefix[::-1]

        return reverse_prefix + other_letters