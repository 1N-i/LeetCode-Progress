class Solution(object):
    def intersection(self, nums1, nums2):
        ans = []

        for num in set(nums1):
            if num in set(nums2): ans.append(num)

        return ans