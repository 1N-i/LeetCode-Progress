class NumArray(object):
    def __init__(self, nums):
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, left, right):
        return self.sums[right + 1] - self.sums[left]