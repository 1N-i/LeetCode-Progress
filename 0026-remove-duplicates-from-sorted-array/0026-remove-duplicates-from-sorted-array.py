class Solution(object):
    def removeDuplicates(self, nums):
        seen = ["_"]
        i, size_control = 0, 0
        while i < len(nums) - size_control:
            if nums[i] not in seen: seen.append(nums[i])
            else:
                if nums[i] == "_": continue
                else:
                    nums.pop(i)
                    i -= 1
                    size_control += 1
                    nums.append("_")
            i += 1

        return len(seen) - 1