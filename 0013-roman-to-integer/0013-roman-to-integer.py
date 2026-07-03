class Solution(object):
    def romanToInt(self, s):
        total = 0
        totalList = []
        romanList = list(s)
        dictRoman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for romanLetter in romanList:
            totalList.append(dictRoman[romanLetter])
        
        for index in range(len(totalList)):
            if index == len(totalList) - 1:
                total += totalList[index]
                break
            
            if totalList[index] >= totalList[index + 1]: total += totalList[index]
            if totalList[index] < totalList[index + 1]: total -= totalList[index]
                
        return total