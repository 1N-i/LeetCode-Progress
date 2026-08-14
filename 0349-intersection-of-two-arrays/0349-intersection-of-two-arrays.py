class Solution(object):
    def intersection(self, nums1, nums2):
        ans = []
        set1, set2 = set(nums1), set(nums2)

        for num in set1:
            if num in set2: ans.append(num)

        return ans