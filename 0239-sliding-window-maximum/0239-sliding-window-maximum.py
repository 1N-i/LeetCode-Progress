class Solution(object):
    def maxSlidingWindow(self, nums, k):
        from collections import deque

        ans, window = [], deque()
        for i in range(len(nums)):
            if window and window[0] <= i - k:
                window.popleft()

            while window and nums[window[-1]] <= nums[i]:
                window.pop()
                
            window.append(i)
            if i >= k - 1:
                ans.append(nums[window[0]])

        return ans