class Solution(object):
    def sortArray(self, nums):
        if len(nums) <= 1: return nums

        mid = len(nums) // 2
        list_l, list_r = self.sortArray(nums[:mid]), self.sortArray(nums[mid:])
        ans = []

        left, right = 0, 0
        while left <= len(list_l) or right <= len(list_r):
            if left >= len(list_l) and right >= len(list_r):
                return ans

            if left >= len(list_l):
                ans.append(list_r[right])
                right += 1
                continue

            if right >= len(list_r):
                ans.append(list_l[left])
                left += 1
                continue

            if list_l[left] < list_r[right]:
                ans.append(list_l[left])
                left += 1
            else:
                ans.append(list_r[right])
                right += 1