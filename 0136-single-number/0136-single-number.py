class Solution(object):
    def singleNumber(self, nums):
        map_nums = {}

        for num in nums:
            map_nums[num] = map_nums.get(num, 0) + 1

        ans = [key for key, qtt in map_nums.items() if qtt == 1]
        return ans[0]