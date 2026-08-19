class Solution(object):
    def duplicateNumbersXOR(self, nums):
        seen, seen_twice = [], []

        for num in nums:
            if num not in seen: seen.append(num)
            else: seen_twice.append(num)

        ans = 0
        for num in seen_twice:
            ans = ans ^ num

        return ans