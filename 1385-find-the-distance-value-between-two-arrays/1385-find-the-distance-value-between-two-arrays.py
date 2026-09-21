class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        ans = len(arr1)

        for num1 in arr1:
            for num2 in arr2:
                dif = num2 - num1
                if dif < 0: dif *= -1
                if dif <= d:
                    ans -= 1
                    break

        return ans