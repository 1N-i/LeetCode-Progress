class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.split(" ")
        
        for word in reversed(s):
            if word != "": return len(word)