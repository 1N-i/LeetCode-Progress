class Solution(object):
    def pivotInteger(self, n):
        for num in range(1, n + 1):
            nums1 = range(1, num + 1)
            nums2 = range(num, n + 1)
            if sum(nums1) == sum(nums2):
                return num

        return -1