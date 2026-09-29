class Solution(object):
    def romanToInt(self, s):
        total = 0
        totalList = []
        dictRoman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for romanLetter in s:
            totalList.append(dictRoman[romanLetter])
        
        for i in range(len(totalList) - 1):
            to_add = totalList[i]
            if to_add >= totalList[i + 1]: total += to_add
            else: total -= to_add
                
        return total + totalList[-1]