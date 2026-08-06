class Solution(object):
    def plusOne(self, digits):
        len_digits = len(digits)
        first_nine = False

        for i in range(len_digits - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                if first_nine == True: digits.pop(i + 1)
                return digits
        
            else:
                print(digits)
                if first_nine == False:
                    digits.pop(i)
                    digits.extend([1, 0])
                    first_nine = True
                
                else: 
                    digits.pop(i)
                    if len(digits) >= 1: digits.pop(i)
                    digits.insert(i, 1)
                    digits.insert(i + 1, 0)

        return digits