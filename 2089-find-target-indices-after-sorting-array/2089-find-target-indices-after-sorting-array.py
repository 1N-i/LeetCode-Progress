class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()

        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)

                for j in range(i + 1, len(nums)):
                    if nums[j] != target: break
                    ans.append(j)

                break

        return ans