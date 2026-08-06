class Solution(object):
    def plusOne(self, digits):
        len_digits = len(digits)

        for i in range(len_digits - 1, -1, -1):
            if i == 0 and digits[0] == 9:
                digits.pop(i)
                digits = [1, 0] + digits

            elif digits[i] != 9:
                digits[i] += 1
                return digits

            else: digits[i] = 0

        
        return digits