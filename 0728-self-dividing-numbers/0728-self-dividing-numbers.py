class Solution(object):
    def selfDividingNumbers(self, left, right):
        ans = [num for num in range(left, right + 1) if self.doesSelfDivide(num)]

        return ans

    def doesSelfDivide(self, n):
        n_str = str(n)
        for num in n_str:
            if num == "0": return False
            if n % int(num) != 0: return False
        
        return True