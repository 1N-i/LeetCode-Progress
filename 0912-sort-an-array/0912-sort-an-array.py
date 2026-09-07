class Solution(object):
    def sortArray(self, nums):
        if len(nums) <= 1: 
            return nums

        mid = len(nums) // 2
        list_l = self.sortArray(nums[:mid])
        list_r = self.sortArray(nums[mid:])
        
        ans = []
        left = right = 0
        
        while left < len(list_l) and right < len(list_r):
            if list_l[left] < list_r[right]:
                ans.append(list_l[left])
                left += 1
            else:
                ans.append(list_r[right])
                right += 1
        
        ans.extend(list_l[left:])
        ans.extend(list_r[right:])
        
        return ans