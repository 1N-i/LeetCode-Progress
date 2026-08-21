class Solution(object):
    def resultArray(self, nums):
        arr1, arr2 = [nums[0]], [nums[1]]

        last_added1, last_added2 = nums[0], nums[1]
        for i in range(2, len(nums)):
            if last_added1 > last_added2:
                arr1.append(nums[i])
                last_added1 = nums[i]
            else:
                arr2.append(nums[i])
                last_added2 = nums[i]

        return arr1 + arr2