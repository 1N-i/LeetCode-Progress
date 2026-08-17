class Solution(object):
    def strStr(self, haystack, needle):
        left, right = 0, len(needle)

        while right <= len(haystack):
            if haystack[left:right] == needle: return left
            left += 1
            right += 1

        return -1