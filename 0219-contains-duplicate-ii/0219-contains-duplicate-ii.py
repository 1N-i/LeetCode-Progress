class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        map_nums = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in map_nums:
                map_nums[nums[i]] = i

            if i - map_nums[num] != 0 and i - map_nums[num] <= k:
                return True
                
            map_nums[num] = i

        return False