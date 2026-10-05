class Solution(object):
    def isPalindrome(self, s):
        text_fixed = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        return text_fixed == text_fixed[::-1]