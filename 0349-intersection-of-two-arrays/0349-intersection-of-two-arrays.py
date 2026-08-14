class Solution(object):
    def intersection(self, nums1, nums2):
        ans = set()
        nums1.sort()
        nums2.sort()

        len1, len2 = len(nums1), len(nums2)

        if len1 > len2:
            for num in nums1:
                if num in nums2: ans.add(num)
        else:
            for num in nums1:
                if num in nums2: ans.add(num)

        return list(ans)