class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        len_nums = len(nums)

        if len_nums % 2 == 0:
            mid = len_nums // 2
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            mid = len_nums // 2
            return nums[mid]