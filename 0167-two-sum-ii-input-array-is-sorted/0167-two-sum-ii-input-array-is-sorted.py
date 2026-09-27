class Solution(object):
    def twoSum(self, nums, target):
        len_nums = len(nums)
        for i in range(len_nums):
            comp = target - nums[i]
            left, right = 0, len_nums - 1
            if nums[i] == comp: return [i + 1, i + 2]
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < comp:
                    left = mid + 1
                elif nums[mid] > comp:
                    right = mid - 1
                else:
                    return [i + 1, mid + 1]