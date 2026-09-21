class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        ans = len(arr1)
        for num1 in arr1:
            valid = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    ans -= 1
                    break

        return ans