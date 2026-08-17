class Solution(object):
    def minimumFlips(self, n):
        binary = bin(n)[2:]
        rev_bin = binary[::-1]
        ans = 0
        
        for i in range(len(binary)):
            if binary[i] != rev_bin[i]: ans += 1

        return ans