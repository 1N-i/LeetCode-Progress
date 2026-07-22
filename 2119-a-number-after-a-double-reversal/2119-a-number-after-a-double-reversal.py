class Solution(object):
    def reversedNum(self, nums):
        reversedx = ""
        for char in nums[::-1]:
            reversedx += char

        return int(reversedx)

    def isSameAfterReversals(self, num):
        reversed1 = self.reversedNum(str(num))
        reversed2 = self.reversedNum(str(reversed1))

        return num == reversed2