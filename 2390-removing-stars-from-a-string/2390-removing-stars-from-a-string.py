class Solution(object):
    def removeStars(self, s):
        ans = []
        
        for char in s:
            if char != "*": ans.append(char)
            else: ans.pop()
                
        return "".join(ans)