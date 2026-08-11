class Solution(object):
    def selfDividingNumbers(self, left, right):
        ans = []

        for num in range(left, right + 1):
            if self.doesSelfDivide(num): ans.append(num)

        return ans

    def doesSelfDivide(self, n):
        n_str = str(n)
        for num in n_str:
            if "0" in num: return False
            if n % int(num) != 0: return False
        
        return True