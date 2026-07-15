class Solution(object):
    def addDigits(self, num):
        if len(str(num)) == 1: return num

        while len(str(num)) != 1:
            num = sum([int(item) for item in list(str(num))])

        return num