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
        
        for i in range(len(totalList)):
            if i == len(totalList) - 1:
                total += totalList[i]
                break
            
            if totalList[i] >= totalList[i + 1]: total += totalList[i]
            if totalList[i] < totalList[i + 1]: total -= totalList[i]
                
        return total