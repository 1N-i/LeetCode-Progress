class Solution(object):
    def kthFactor(self, n, k):
        ans = []

        for num in range(1, n + 1):
            if n % num == 0: ans.append(num)

        if len(ans) < k: return -1
        return ans[k - 1]