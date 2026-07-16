class Solution(object):
    def findGCD(self, nums):
        minNum = min(nums)
        maxNum = max(nums)

        if maxNum % minNum == 0: return minNum
        
        divisors = []
        for num in range(2, maxNum):
            if minNum % num == 0 and maxNum % num == 0:
                divisors.append(num)
                
        if len(divisors) != 0: return max(divisors)

        return 1