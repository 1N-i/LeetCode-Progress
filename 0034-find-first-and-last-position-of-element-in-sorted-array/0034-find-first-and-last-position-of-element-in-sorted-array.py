class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 0: return [-1, -1]

        left, right = 0, len(nums) - 1
        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target:
                mid_id = mid
                break #Finds one of the index
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if nums[mid] != target: return [-1, -1]

        left, right = 0, mid_id
        while left < right: #Finds the min index
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            else:
                left = mid + 1
        left_id = left

        left, right = mid_id, len(nums) - 1
        while left < right: #Finds the max index
            mid = ((left + right) // 2) + 1
            if nums[mid] == target:
                left = mid
            else:
                right = mid - 1
        right_id = left

        return left_id, right_id