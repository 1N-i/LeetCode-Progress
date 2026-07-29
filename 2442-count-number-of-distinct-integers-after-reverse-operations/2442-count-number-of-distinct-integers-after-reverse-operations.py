class Solution(object):
    def countDistinctIntegers(self, nums):
        nums_and_reverse = nums[:]
        for num in nums:
            nums_and_reverse.append(self.reverseNum(str(num)))

        seen = set()
        for num in nums_and_reverse:
            seen.add(num)

        return len(seen)

    def reverseNum(self, str_num):
        return int(str_num[::-1])