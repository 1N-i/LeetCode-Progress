class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        map_nums = {}
        for i in range(len(nums)):
            if nums[i] not in map_nums:
                map_nums[nums[i]] = i
            else:
                if i - map_nums[nums[i]] <= k: return True
                map_nums[nums[i]] = i

        return False