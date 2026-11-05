class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()
        ans = len(arr1)
        for num1 in arr1:
            for i in range(len(arr2) - 1, -1, -1):
                if abs(num1 - arr2[i]) <= d:
                    ans -= 1
                    break

        return ans