class Solution(object):
    def intersection(self, nums1, nums2):
        ans = []
        set1 = set(nums1)

        for num in set1:
            if num in set(nums2): ans.append(num)

        return ans