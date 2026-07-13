class Solution(object):
    def convertDateToBinary(self, date):
        list_date = date.replace("-", " - ").split(" ")
        ans = ""
        
        for i in range(5):
            if i == 1 or i == 3: ans += "-"
            else: ans += bin(int(list_date[i]))[2:]

        return ans