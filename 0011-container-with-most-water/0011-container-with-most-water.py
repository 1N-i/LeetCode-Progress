class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        curr_max = 0

        while left <= right:
            curr = min(height[left], height[right]) * (right - left)
            if curr_max < curr:
                curr_max = curr

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return curr_max