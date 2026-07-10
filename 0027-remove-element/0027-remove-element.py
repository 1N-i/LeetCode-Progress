class Solution(object):
    def removeElement(self, nums, val):
        correct_nums = []
        underscore_qt = 0

        for num in nums:
            if num != val:
                correct_nums.append(num)
            else:
                underscore_qt += 1

        nums[:] = correct_nums

        return len(nums)