class Solution(object):
    def duplicateNumbersXOR(self, nums):
        seen, seen_twice = [], []
        ans = 0

        for num in nums:
            if num not in seen: seen.append(num)
            else: ans = ans ^ num

        return ans