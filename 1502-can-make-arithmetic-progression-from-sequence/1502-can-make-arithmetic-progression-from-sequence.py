class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        dist = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != dist:
                return False
        
        return True