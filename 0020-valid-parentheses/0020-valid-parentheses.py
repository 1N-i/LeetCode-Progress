class Solution(object):
    def isValid(self, s):
        if len(s) <= 1: return False
        if s[-1] in ["(", "[", "{"]: return False
        if s[0] in [")", "]", "}"]: return False

        guide = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        look = []
        for char in s:
            if char in guide:
                if len(look) == 0 or look[-1] != guide[char]:
                    return False
                look.pop()
        
            else:
                look.append(char)

        return len(look) == 0