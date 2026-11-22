class Solution(object):
    def checkString(self, s):
        seen_b = False

        for l in s:
            if l == "b":
                seen_b = True
                
            if seen_b == True and l == "a":
                return False

        return True