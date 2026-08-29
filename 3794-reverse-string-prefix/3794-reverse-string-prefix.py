class Solution:
    def reversePrefix(self, s, k):
        ans = list(s)
        left, right = 0, k - 1

        while left < right:
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1

        return "".join(ans)