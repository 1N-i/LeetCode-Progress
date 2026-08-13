class Solution(object):
    def shuffle(self, nums, n):
        x_nums, y_nums = nums[:n], nums[n:]
        ans = []

        for i in range(n):
            ans.append(x_nums[i])
            ans.append(y_nums[i])

        return ans