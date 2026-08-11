class Solution(object):
    def selfDividingNumbers(self, left, right):
        nums = list(range(left, right + 1))
        ans = []

        for num in nums:
            if self.doesSelfDivide(num): ans.append(num)

        return ans

    def doesSelfDivide(self, n):
        n_list = list(str(n))
        for num in n_list:
            if "0" in num: return False
            if n % int(num) != 0: return False
        
        return True