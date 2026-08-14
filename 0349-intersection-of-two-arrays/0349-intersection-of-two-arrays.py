class Solution(object):
    def intersection(self, nums1, nums2):
        ans = set()
        nums1.sort()
        nums2.sort()

        for num in nums1:
            if num in nums2: ans.add(num)

        return list(ans)