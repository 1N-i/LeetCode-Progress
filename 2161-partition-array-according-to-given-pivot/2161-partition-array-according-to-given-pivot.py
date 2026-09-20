class Solution(object):
    def pivotArray(self, nums, pivot):
        buckets = [[], [], []]

        for num in nums:
            if num < pivot:
                buckets[0].append(num)
            elif num == pivot:
                buckets[1].append(num)
            else:
                buckets[2].append(num)

        return buckets[0] + buckets[1] + buckets[2]