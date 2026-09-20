class Solution(object):
    def pivotArray(self, nums, pivot):
        smaller, equal, bigger = [], [], []
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                bigger.append(num)

        return smaller + equal + bigger