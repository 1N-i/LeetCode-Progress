class Solution(object):
    def addDigits(self, num):
        while len(str(num)) != 1:
            new_num = list(str(num))
            num = sum([int(item) for item in new_num])
            
        return num